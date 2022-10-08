import factory

from faker import Faker
from user.models import YelpUser

fake = Faker()

class YelpUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = YelpUser

    user_id = factory.LazyAttribute(lambda _: fake.bothify(text='??????????????????????'))
    name = factory.LazyAttribute(lambda _: fake.name())
    review_count = factory.LazyAttribute(lambda _: fake.random_digit())
    yelping_since = factory.LazyAttribute(lambda _: fake.date_time_ad())
    useful = factory.LazyAttribute(lambda _: fake.random_digit())
    funny = factory.LazyAttribute(lambda _: fake.random_digit())
    cool = factory.LazyAttribute(lambda _: fake.random_digit())
    fans = factory.LazyAttribute(lambda _: fake.random_digit())
    friends = factory.LazyAttribute(lambda _: fake.bothify(text='??????????????????????'))
    elite = factory.LazyAttribute(lambda _: fake.bothify(text='??????????????????????'))
    average_stars = factory.LazyAttribute(lambda _: fake.pyfloat(positive=True))
    compliment_hot = factory.LazyAttribute(lambda _: fake.random_digit())
    compliment_more = factory.LazyAttribute(lambda _: fake.random_digit())
    compliment_profile = factory.LazyAttribute(lambda _: fake.random_digit())
    compliment_cute = factory.LazyAttribute(lambda _: fake.random_digit())
    compliment_list = factory.LazyAttribute(lambda _: fake.random_digit())
    compliment_note = factory.LazyAttribute(lambda _: fake.random_digit())
    compliment_plain = factory.LazyAttribute(lambda _: fake.random_digit())
    compliment_cool = factory.LazyAttribute(lambda _: fake.random_digit())
    compliment_funny = factory.LazyAttribute(lambda _: fake.random_digit())
    compliment_writer = factory.LazyAttribute(lambda _: fake.random_digit())
    compliment_photos = factory.LazyAttribute(lambda _: fake.random_digit())
