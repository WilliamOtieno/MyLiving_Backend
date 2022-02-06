import json

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from ..models import Building
from ..serializers import BuildingSerializer

client = APIClient()


class TestBuildingCreateAPIView(APITestCase):
    def setUp(self) -> None:
        self.valid_payload = {
            "name": "Test Building",
            "description": "Deluxe Maisonette"
        }
        self.invalid_payload = {
            "description": "Deluxe Maisonette",
            "tenant_number": "Two Tenants"
        }
        self.valid_payload = json.dumps(self.valid_payload)

    def test_create_valid_object(self):
        response = client.post(reverse('housing:building_create'), data=self.valid_payload,
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_object(self):
        response = client.post(reverse('housing:building_create'), data=self.invalid_payload,
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestBuildingRetrieveAPIView(APITestCase):
    def setUp(self) -> None:
        self.building1 = Building.objects.create(name='Test Building 1', description='Test Description 1',
                                                 location='Location 1',
                                                 gps_coordinates='12346,123462')
        self.building2 = Building.objects.create(name='Test Building 2', description='Test Description 2',
                                                 location='Location 2',
                                                 gps_coordinates='12346,123462')
        self.building3 = Building.objects.create(name='Test Building 3', description='Test Description 3',
                                                 location='Location 3',
                                                 gps_coordinates='12346,123462')

    def test_get_valid_object(self):
        response = client.get(reverse('housing:building_retrieve', kwargs={'pk': self.building1.pk}))
        building = Building.objects.get(pk=self.building1.pk)
        serializer = BuildingSerializer(building, many=False)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_object(self):
        response = client.get(reverse('housing:building_retrieve', kwargs={'pk': '30'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TestBuildingUpdateAPIView(APITestCase):
    def setUp(self) -> None:
        self.building1 = Building.objects.create(name='Test Building 1', description='Test Description 1',
                                                 location='Location 1',
                                                 gps_coordinates='12346,123462')
        self.valid_payload = {
            "name": "Test Building",
            "description": "Deluxe Maisonette"
        }
        self.invalid_payload = {
            "description": "Deluxe Maisonette",
            "tenant_number": "Two Tenants"
        }
        self.valid_payload = json.dumps(self.valid_payload)

    def test_valid_update(self):
        response = client.put(reverse('housing:building_update', kwargs={'pk': self.building1.pk}),
                              data=self.valid_payload, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update(self):
        response = client.put(reverse('housing:building_update', kwargs={'pk': self.building1.pk}),
                              data=self.invalid_payload, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_non_existent_update(self):
        response = client.put(reverse('housing:building_update', kwargs={'pk': '30'}),
                              data=self.valid_payload, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TestBuildingDeleteAPIView(APITestCase):
    def setUp(self) -> None:
        self.building1 = Building.objects.create(name='Test Building 1', description='Test Description 1',
                                                 location='Location 1',
                                                 gps_coordinates='12346,123462')

    def test_valid_delete(self):
        response = client.delete(reverse('housing:building_delete', kwargs={'pk': self.building1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_non_existent_delete(self):
        response = client.delete(reverse('housing:building_delete', kwargs={'pk': '30'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TestBuildingListAPIView(APITestCase):
    def setUp(self) -> None:
        Building.objects.create(name='Test Building 1', description='Test Description 1', location='Location 1',
                                gps_coordinates='12346,123462')
        Building.objects.create(name='Test Building 2', description='Test Description 2', location='Location 2',
                                gps_coordinates='12346,123462')
        Building.objects.create(name='Test Building 3', description='Test Description 3', location='Location 3',
                                gps_coordinates='12346,123462')

    def test_all_buildings_fetched(self):
        buildings = Building.objects.all()
        serializer = BuildingSerializer(buildings, many=True)

        response = client.get(reverse('housing:building_list'))
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(buildings.count(), 3)
