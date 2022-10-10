from django.test import TestCase

from .factories import BusinessFactory
from general.tests.user_factories import UserFactory
from general.tests.tests_base import YelpTestCase
from .serializers import BusinessListSerializer, BusinessDetailSerializer


class BusinessListSerializerSerializerTests(TestCase):
    """Test the correct operation of the BusinessDetailSerializer"""

    def setUp(self) -> None:
        self.business = BusinessFactory()

    def test_serializer_contains_expected_fields(self):
        serializer = BusinessListSerializer(instance=self.business)

        self.assertCountEqual(
            serializer.data.keys(),
            [
                "business_id",
                "name",
                "address",
                "city",
                "state",
                "postal_code",
                "latitude",
                "longitude",
                "stars",
                "review_count",
                "is_open",
            ],
        )

    def test_serialize_object_properly(self):
        serializer = BusinessListSerializer(instance=self.business)
        data = serializer.data

        self.assertEquals(data["business_id"], self.business.business_id)
        self.assertEquals(data["name"], self.business.name)
        self.assertEquals(data["address"], self.business.address)
        self.assertEquals(data["city"], self.business.city)
        self.assertEquals(data["state"], self.business.state)
        self.assertEquals(data["postal_code"], self.business.postal_code)
        self.assertEquals(data["latitude"], float(self.business.latitude))
        self.assertEquals(data["longitude"], float(self.business.longitude))
        self.assertEquals(data["stars"], float(self.business.stars))
        self.assertEquals(data["stars"], self.business.stars)
        self.assertEquals(data["review_count"], self.business.review_count)
        self.assertEquals(data["is_open"], self.business.is_open)


class BusinessDetailSerializerSerializerTests(TestCase):
    """Test the correct operation of the BusinessDetailSerializer"""

    def setUp(self) -> None:
        self.business = BusinessFactory()

    def test_serializer_contains_expected_fields(self):
        serializer = BusinessDetailSerializer(instance=self.business)

        self.assertCountEqual(
            serializer.data.keys(),
            [
                "business_id",
                "name",
                "address",
                "city",
                "state",
                "postal_code",
                "latitude",
                "longitude",
                "stars",
                "review_count",
                "is_open",
                "attributes",
                "categories",
                "hours",
            ],
        )

    def test_serialize_object_properly(self):
        serializer = BusinessDetailSerializer(instance=self.business)
        data = serializer.data

        self.assertEquals(data["business_id"], self.business.business_id)
        self.assertEquals(data["name"], self.business.name)
        self.assertEquals(data["address"], self.business.address)
        self.assertEquals(data["city"], self.business.city)
        self.assertEquals(data["state"], self.business.state)
        self.assertEquals(data["postal_code"], self.business.postal_code)
        self.assertEquals(data["latitude"], float(self.business.latitude))
        self.assertEquals(data["longitude"], float(self.business.longitude))
        self.assertEquals(data["stars"], float(self.business.stars))
        self.assertEquals(data["review_count"], self.business.review_count)
        self.assertEquals(data["is_open"], self.business.is_open)
        self.assertEquals(data["attributes"], self.business.attributes)
        self.assertEquals(data["categories"], self.business.categories)
        self.assertEquals(data["hours"], self.business.hours)


class BusinessViewsetTestCase(YelpTestCase):
    def setUp(self):
        self.user = UserFactory()
        self.business_1 = BusinessFactory()
        for i in range(0, 9):
            BusinessFactory(name=str(i))
        self.url = "/api/business/"

    def test_list_view(self):
        """Test that the list view works correctly"""
        token = self.authenticate(self.user)
        response = self.client.get(self.url, HTTP_AUTHORIZATION=token)
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["count"], 10)

    def test_detail_view(self):
        """Test that the detail view works correctly"""
        token = self.authenticate(self.user)
        response = self.client.get(
            f"{self.url}{self.business_1.business_id}/", HTTP_AUTHORIZATION=token
        )
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEquals(data["business_id"], self.business_1.business_id)
        self.assertEquals(data["name"], self.business_1.name)
        self.assertEquals(data["address"], self.business_1.address)
        self.assertEquals(data["city"], self.business_1.city)
        self.assertEquals(data["state"], self.business_1.state)
        self.assertEquals(data["postal_code"], self.business_1.postal_code)
        self.assertEquals(data["latitude"], float(self.business_1.latitude))
        self.assertEquals(data["longitude"], float(self.business_1.longitude))
        self.assertEquals(data["stars"], float(self.business_1.stars))
        self.assertEquals(data["review_count"], self.business_1.review_count)
        self.assertEquals(data["is_open"], self.business_1.is_open)
        self.assertEquals(data["attributes"], self.business_1.attributes)
        self.assertEquals(data["categories"], self.business_1.categories)
        self.assertEquals(data["hours"], self.business_1.hours)
