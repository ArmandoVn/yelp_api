from django.test import TestCase

from .factories import YelpUserFactory
from general.tests.user_factories import UserFactory
from general.tests.tests_base import YelpTestCase
from .serializers import YelpUserDetailSerializer, YelpUserListSerializer

class YelpUserListSerializerSerializerTests(TestCase):
    """ Test the correct operation of the YelpUserListSerializer """
    def setUp(self) -> None:
        self.yelp_user = YelpUserFactory()

    def test_serializer_contains_expected_fields(self):
        serializer = YelpUserListSerializer(instance=self.yelp_user)

        self.assertCountEqual(
            serializer.data.keys(),
            [
                'user_id',
                'name',
                'review_count',
                'yelping_since',
                'useful',
                'funny',
                'cool',
                'fans',
                'elite',
                'average_stars',
                'compliment_hot',
                'compliment_more',
                'compliment_profile',
                'compliment_cute',
                'compliment_list',
                'compliment_note',
                'compliment_plain',
                'compliment_cool',
                'compliment_funny',
                'compliment_writer',
                'compliment_photos',
            ],
        )

    def test_serialize_object_properly(self):
        serializer = YelpUserListSerializer(instance=self.yelp_user)
        data = serializer.data

        self.assertEquals(data['user_id'], self.yelp_user.user_id)
        self.assertEquals(data['name'], self.yelp_user.name)
        self.assertEquals(data['review_count'], self.yelp_user.review_count)
        self.assertEquals(data['useful'], self.yelp_user.useful)
        self.assertEquals(data['funny'], self.yelp_user.funny)
        self.assertEquals(data['cool'], self.yelp_user.cool)
        self.assertEquals(data['fans'], self.yelp_user.fans)
        self.assertEquals(data['elite'], self.yelp_user.elite)
        self.assertEquals(data['average_stars'], float(self.yelp_user.average_stars))
        self.assertEquals(data['compliment_hot'], self.yelp_user.compliment_hot)
        self.assertEquals(data['compliment_more'], self.yelp_user.compliment_more)
        self.assertEquals(data['compliment_profile'], self.yelp_user.compliment_profile)
        self.assertEquals(data['compliment_cute'], self.yelp_user.compliment_cute)
        self.assertEquals(data['compliment_list'], self.yelp_user.compliment_list)
        self.assertEquals(data['compliment_note'], self.yelp_user.compliment_note)
        self.assertEquals(data['compliment_plain'], self.yelp_user.compliment_plain)
        self.assertEquals(data['compliment_cool'], self.yelp_user.compliment_cool)
        self.assertEquals(data['compliment_funny'], self.yelp_user.compliment_funny)
        self.assertEquals(data['compliment_writer'], self.yelp_user.compliment_writer)
        self.assertEquals(data['compliment_photos'], self.yelp_user.compliment_photos)


class YelpUserDetailSerializerSerializerTests(TestCase):
    """ Test the correct operation of the YelpUserDetailSerializer """
    def setUp(self) -> None:
        self.yelp_user = YelpUserFactory()

    def test_serializer_contains_expected_fields(self):
        serializer = YelpUserDetailSerializer(instance=self.yelp_user)

        self.assertCountEqual(
            serializer.data.keys(),
            [
                'user_id',
                'name',
                'review_count',
                'yelping_since',
                'useful',
                'funny',
                'cool',
                'fans',
                'friends',
                'elite',
                'average_stars',
                'compliment_hot',
                'compliment_more',
                'compliment_profile',
                'compliment_cute',
                'compliment_list',
                'compliment_note',
                'compliment_plain',
                'compliment_cool',
                'compliment_funny',
                'compliment_writer',
                'compliment_photos',
            ],
        )

    def test_serialize_object_properly(self):
        serializer = YelpUserDetailSerializer(instance=self.yelp_user)
        data = serializer.data

        self.assertEquals(data['user_id'], self.yelp_user.user_id)
        self.assertEquals(data['name'], self.yelp_user.name)
        self.assertEquals(data['review_count'], self.yelp_user.review_count)
        self.assertEquals(data['useful'], self.yelp_user.useful)
        self.assertEquals(data['funny'], self.yelp_user.funny)
        self.assertEquals(data['cool'], self.yelp_user.cool)
        self.assertEquals(data['fans'], self.yelp_user.fans)
        self.assertEquals(data['elite'], self.yelp_user.elite)
        self.assertEquals(data['friends'], self.yelp_user.friends)
        self.assertEquals(data['average_stars'], float(self.yelp_user.average_stars))
        self.assertEquals(data['compliment_hot'], self.yelp_user.compliment_hot)
        self.assertEquals(data['compliment_more'], self.yelp_user.compliment_more)
        self.assertEquals(data['compliment_profile'], self.yelp_user.compliment_profile)
        self.assertEquals(data['compliment_cute'], self.yelp_user.compliment_cute)
        self.assertEquals(data['compliment_list'], self.yelp_user.compliment_list)
        self.assertEquals(data['compliment_note'], self.yelp_user.compliment_note)
        self.assertEquals(data['compliment_plain'], self.yelp_user.compliment_plain)
        self.assertEquals(data['compliment_cool'], self.yelp_user.compliment_cool)
        self.assertEquals(data['compliment_funny'], self.yelp_user.compliment_funny)
        self.assertEquals(data['compliment_writer'], self.yelp_user.compliment_writer)
        self.assertEquals(data['compliment_photos'], self.yelp_user.compliment_photos)


class YelpUserViewsetTestCase(YelpTestCase):
    def setUp(self):
        self.user = UserFactory()
        self.yelp_user_1 = YelpUserFactory()
        for i in range(0, 9):
            YelpUserFactory(name=str(i))
        self.url = "/api/users/"

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
        response = self.client.get(f"{self.url}{self.yelp_user_1.user_id}/", HTTP_AUTHORIZATION=token)
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEquals(data['user_id'], self.yelp_user_1.user_id)
        self.assertEquals(data['name'], self.yelp_user_1.name)
        self.assertEquals(data['review_count'], self.yelp_user_1.review_count)
        self.assertEquals(data['useful'], self.yelp_user_1.useful)
        self.assertEquals(data['funny'], self.yelp_user_1.funny)
        self.assertEquals(data['cool'], self.yelp_user_1.cool)
        self.assertEquals(data['fans'], self.yelp_user_1.fans)
        self.assertEquals(data['elite'], self.yelp_user_1.elite)
        self.assertEquals(data['friends'], self.yelp_user_1.friends)
        self.assertEquals(data['average_stars'], float(self.yelp_user_1.average_stars))
        self.assertEquals(data['compliment_hot'], self.yelp_user_1.compliment_hot)
        self.assertEquals(data['compliment_more'], self.yelp_user_1.compliment_more)
        self.assertEquals(data['compliment_profile'], self.yelp_user_1.compliment_profile)
        self.assertEquals(data['compliment_cute'], self.yelp_user_1.compliment_cute)
        self.assertEquals(data['compliment_list'], self.yelp_user_1.compliment_list)
        self.assertEquals(data['compliment_note'], self.yelp_user_1.compliment_note)
        self.assertEquals(data['compliment_plain'], self.yelp_user_1.compliment_plain)
        self.assertEquals(data['compliment_cool'], self.yelp_user_1.compliment_cool)
        self.assertEquals(data['compliment_funny'], self.yelp_user_1.compliment_funny)
        self.assertEquals(data['compliment_writer'], self.yelp_user_1.compliment_writer)
        self.assertEquals(data['compliment_photos'], self.yelp_user_1.compliment_photos)
