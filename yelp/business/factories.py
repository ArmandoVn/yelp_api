import factory

from faker import Faker
from business.models import Business

fake = Faker()

class BusinessFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Business

    business_id = factory.LazyAttribute(lambda _: fake.bothify(text='??????????????????????'))
    name = factory.LazyAttribute(lambda _: fake.name())
    address = factory.LazyAttribute(lambda _: fake.street_address())
    city = factory.LazyAttribute(lambda _: fake.city())
    state = factory.LazyAttribute(lambda _: fake.city())
    postal_code = factory.LazyAttribute(lambda _: fake.postcode())
    latitude = factory.LazyAttribute(lambda _: fake.latitude())
    longitude = factory.LazyAttribute(lambda _: fake.longitude())
    stars = factory.LazyAttribute(lambda _: fake.random_digit())
    review_count = factory.LazyAttribute(lambda _: fake.random_digit())
    is_open = factory.LazyAttribute(lambda _: fake.random_element(elements=(1, 2)))
