from lxml.builder import E
from iati.models import Activity
from iati_synchroniser.factory.synchroniser_factory import DatasetFactory
from iati_codelists.factory.codelist_factory import VersionFactory
from mock import MagicMock
import datetime
from iati.parser.IATI_2_01 import Parse as Parser_201
from iati.factory import iati_factory
from django.test import TestCase


class PostSaveFileTestCase(TestCase):
    """
    2.01: post save activity actions called
    """

    def setUp(self):
        self.iati_source = DatasetFactory.create(ref='source_reference')
        version = VersionFactory(code='2.01')
        self.first_activity = iati_factory.ActivityFactory.create(
            id='IATI-0001',
            iati_identifier='IATI-0001',
            iati_standard_version=version,
            name='source_reference')
        self.second_activity = iati_factory.ActivityFactory.create(
            id='IATI-0002',
            iati_identifier='IATI-0002',
            iati_standard_version=self.first_activity.iati_standard_version,
            name='source_reference')

    def test_post_save_file(self):
        """
        Check if all required functions are called
        """
        self.parser = Parser_201(None)
        self.parser.iati_source = self.iati_source
        self.parser.delete_removed_activities = MagicMock()
        self.parser.post_save_file(self.parser.iati_source)
        self.parser.delete_removed_activities.assert_called_once_with('source_reference')

    def test_delete_removed_activities(self):
        """The parser should remove activities that are not in the source any longer

        create 2 activities
        mock a file with 1 of them
        parsing this file should delete the other activity
        """
        root = E('iati-activities', version='2.01')
        xml_activity = E('iati-activity')
        xml_title = E('title', 'Title of activity 1')
        xml_activity.append(xml_title)
        xml_identifier = E('iati-identifier', 'IATI-0001')
        xml_activity.append(xml_identifier)
        root.append(xml_activity)

        self.parser = Parser_201(root)
        self.parser.iati_source = self.iati_source
        # mock non related functions that are called (and that use postgres fts which makes the test fail on sqlite)
        self.parser.update_activity_search_index = MagicMock()
        self.parser.post_save_models = MagicMock()

        self.parser.parse_start_datetime = datetime.datetime.now()
        self.parser.parse_activities(root)

        self.assertEqual(Activity.objects.count(), 1)
