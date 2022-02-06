import uuid
import datetime

from django.test import TestCase
from housing.models import Building


class TestBuilding(TestCase):
    def setUp(self) -> None:
        Building.objects.create(name='Test Building 1', description='Test Description 1', location='Location 1',
                                gps_coordinates='12346,123462')
        Building.objects.create(name='Test Building 2', description='Test Description 2', location='Location 2',
                                gps_coordinates='12346,123462')
        Building.objects.create(name='Test Building 3', description='Test Description 3', location='Location 3',
                                gps_coordinates='12346,123462')

    def test_object_count(self):
        self.assertEqual(Building.objects.all().count(), 3)

    def test_objects_were_created(self):
        self.assertTrue(Building.objects.all().exists())

    def test_field_types(self):
        obj = Building.objects.all().last()
        self.assertIsInstance(obj.uuid, uuid.UUID)
        self.assertIsInstance(obj.name, str)
        self.assertIsInstance(obj.description, str)
        self.assertIsInstance(obj.tenant_number, int)
        self.assertGreaterEqual(obj.tenant_number, 0)
        self.assertIsInstance(obj.location, str)
        self.assertIsInstance(obj.gps_coordinates, str)
        self.assertIsInstance(obj.created, datetime.datetime)
        self.assertIsInstance(obj.updated, datetime.datetime)

    def test_object_fields(self):
        obj = Building.objects.all().first()
        self.assertEqual(obj.name, 'Test Building 1')
        self.assertEqual(obj.description, 'Test Description 1')
        self.assertEqual(obj.tenant_number, 0)
        self.assertEqual(obj.location, 'Location 1')
        self.assertEqual(obj.gps_coordinates, '12346,123462')

    def test_object_representation(self):
        obj = Building.objects.all().last()
        self.assertEqual(obj.__str__(), obj.name)
