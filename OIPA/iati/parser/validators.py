import re
from iati import models
from iati.transaction import models as transaction_models
from iati_codelists import models as codelist_models
from iati_vocabulary import models as vocabulary_models
from iati_organisation import models as organisation_models
import dateutil.parser

from iati.parser.exceptions import *

def get_or_raise(model, validated_data, attr, default=None):
    try:
        pk = validated_data.pop(attr)
    except KeyError:
        raise RequiredFieldError(
                model.__name__,
                attr,
                )

    return model.objects.get(pk=pk)
    # except model.DoesNotExist:
    #     return default


def get_or_none(model, validated_data, attr, default=None):
    pk = validated_data.pop(attr, None)

    if pk is None:
        return default
    try:
        return model.objects.get(pk=pk)
    except model.DoesNotExist:
        return default

def get_or_none(model, *args, **kwargs):
    try:
        return model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        return None

def normalize(attr): 
    attr = attr.strip(' \t\n\r').replace(" ", "")
    attr = re.sub("[/:',.+]", "-", attr)
    return attr

def makeBool(text):
    if type(text) == bool:
        return text
    if text == '1' or text == 'true':
        return True
    return False

def makeBoolNone(text):
    if type(text) == bool:
        return text
    if text == '1':
        return True
    elif text == '0':
        return False

    return None

def validate_date(unvalidated_date):

    if unvalidated_date:
        unvalidated_date = unvalidated_date.strip(' \t\n\rZ')
    else:
        return None

    #check if standard data parser works
    try:
        date = dateutil.parser.parse(unvalidated_date, ignoretz=True)
        if date.year >= 1900 and date.year <= 2100:
            return date
        else:
            return None
    except:
        raise RequiredFieldError(
                "TO DO",
                "iso-date",
                "Unspecified or invalid. Date should be of type xml:date.")


def narrative(activity, default_lang, lang, text):
    warnings = []
    errors = []

    if lang:
        lang = lang.lower()

    language = get_or_none(codelist_models.Language, code=lang)

    if not language:
        language = default_lang

    if not language:
        errors.append(
            RequiredFieldError(
                "narrative",
                "xml:lang",
                "must specify xml:lang on iati-activity or xml:lang on the element itself",
                ))

    if not text:
        errors.append(
            RequiredFieldError(
                'narrative',
                "text", 
                "empty narrative",
                ))
    
    return {
        "warnings": warnings,
        "errors": errors,
        "validated_data": {
            "language": language,
            "content": text,
        }
    }

def narratives(activity, narratives):
    warnings = []
    errors = []
    validated_data = []

    default_lang = activity.default_lang

    for n in narratives:
        print(n)
        validated = narrative(activity, default_lang, n.get('language', {}).get('code'), n.get('content'))
        warnings = warnings + validated['warnings']
        errors = errors + validated['errors']
        validated_data.append(validated['validated_data'])

    return {
        "warnings": warnings,
        "errors": errors,
        "validated_data": validated_data,
    }

def codelist(iati_name, model, code):
    warnings = []
    errors = []

    if not code:
        errors.append(
            RequiredFieldError(
                iati_name,
                "ref",
                ))
    
    instance = get_or_none(model, pk=code)

    if not instance:
        errors.append(
            RequiredFieldError(
                iati_name,
                "code",
                "not found on the accompanying code list"
                ))

    return {
        "warnings": warnings,
        "errors": errors,
        "validated_data": instance,
    }


def activity(
        iati_identifier,
        default_lang,
        hierarchy,
        humanitarian,
        last_updated_datetime,
        linked_data_uri,
        default_currency,
        xml_source_ref=None, # if parsed
        activity_status=None,
        iati_standard_version="2.02",
        published=False,
        ):

        warnings = []
        errors = []

        if not hierarchy: hierarchy = 1

        default_currency = get_or_none(models.Currency, pk=default_currency)
        iati_standard_version = get_or_none(models.Version, pk=iati_standard_version)
        activity_status = get_or_none(models.ActivityStatus, pk=activity_status)

        try:
            last_updated_datetime = validate_date(last_updated_datetime)
        except RequiredFieldError:
            errors.append(
                RequiredFieldError(
                    "activity",
                    "last-updated-datetime",
                    "invalid date",
                    ))
            last_updated_datetime = None


        activity_id = normalize(iati_identifier)

        if not activity_id:
            errors.append(
                RequiredFieldError(
                    "activity",
                    "iati-identifier",
                    ))

        instance = models.Activity()
        instance.id = activity_id
        instance.iati_identifier = iati_identifier
        instance.default_lang = default_lang
        instance.hierarchy = hierarchy
        instance.humanitarian = makeBoolNone(humanitarian)
        instance.xml_source_ref = xml_source_ref
        instance.last_updated_datetime = last_updated_datetime
        instance.linked_data_uri = linked_data_uri
        instance.default_currency = default_currency
        instance.iati_standard_version_id = iati_standard_version
        instance.published = published

        return {
            "warnings": warnings,
            "errors": errors,
            "validated_data": {
                "id": activity_id,
                "iati_identifier": iati_identifier,
                "default_lang": default_lang,
                "hierarchy": hierarchy,
                "humanitarian": humanitarian,
                "xml_source_ref": xml_source_ref,
                "last_updated_datetime": last_updated_datetime,
                "linked_data_uri": linked_data_uri,
                "default_currency": default_currency,
                "activity_status": activity_status,
                "iati_standard_version_id": iati_standard_version,
                "published": published,
            },
        }

def activity_status(code):
    return codelist('activity-status', codelist_models.ActivityStatus, code)



def activity_reporting_org(
        activity,
        ref,
        org_type,
        secondary_reporter,
        ):

        organisation = get_or_none(models.Organisation, pk=ref)
        org_type = get_or_none(codelist_models.OrganisationType, code=org_type)

        warnings = []
        errors = []

        if not ref:
            errors.append(
                RequiredFieldError(
                    "reporting-org",
                    "ref",
                    ))

        if not org_type:
            errors.append(
                RequiredFieldError(
                    "reporting-org",
                    "type",
                    ))

        if not secondary_reporter:
            secondary_reporter = False

        if not organisation:
            warnings.append(
                RequiredFieldError(
                    "reporting-org",
                    "organisation",
                    "organisation with ref {} does not exist in organisation standard".format(ref)
                    ))

        # instance = models.ActivityReportingOrganisation()
        # instance.ref = ref
        # instance.normalized_ref = normalize(ref)
        # instance.type = org_type  
        # instance.activity = activity
        # instance.organisation = organisation
        # instance.secondary_reporter = makeBool(secondary_reporter)


        return {
            "warnings": warnings,
            "errors": errors,
            "validated_data": { # maps to model fields
                "activity": activity,
                "ref": ref,
                "normalized_ref": normalize(ref),
                "type": org_type,
                "secondary_reporter": secondary_reporter,
                "organisation": organisation,
            }
        }
        


def activity_description(
        activity,
        type_code=0,
        ):

        description_type = get_or_none(models.DescriptionType, code=type_code)

        warnings = []
        errors = []

        return {
            "warnings": warnings,
            "errors": errors,
            "validated_data": {
                "activity": activity,
                "type": description_type
            },
        }


def activity_participating_org(
        activity,
        ref,
        org_type,
        org_role,
        org_activity_id=None,
        ):

        organisation = get_or_none(models.Organisation, pk=ref)
        org_type = get_or_none(codelist_models.OrganisationType, code=org_type)
        org_role = get_or_none(codelist_models.OrganisationRole, code=org_role)

        warnings = []
        errors = []

        # NOTE: strictly taken, the ref should be specified. In practice many reporters don't use them
        # simply because they don't know the ref.
        if not ref:
            warnings.append(
                RequiredFieldError(
                    "reporting-org",
                    "ref",
                    ))

        if not org_type:
            warnings.append(
                RequiredFieldError(
                    "reporting-org",
                    "type",
                    ))

        if not org_role:
            errors.append(
                RequiredFieldError(
                    "reporting-org",
                    "role",
                    ))

        if not organisation:
            warnings.append(
                RequiredFieldError(
                    "reporting-org",
                    "organisation",
                    "organisation with ref {} does not exist in organisation standard".format(ref)
                    ))

        return {
            "warnings": warnings,
            "errors": errors,
            "validated_data": {
                "ref": ref,
                "normalized_ref": normalize(ref),
                "type": org_type,
                "role": org_role,
                "activity": activity,
                "organisation": organisation,
                "org_activity_id": org_activity_id,
            },
        }
 