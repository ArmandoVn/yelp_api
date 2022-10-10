
# Yelp API

![Logo](https://s3-media0.fl.yelpcdn.com/assets/public/960x225_dataset.yji-04eb5a6d4caf0ee710b34bbb37d3f4cf.png)

This is an API Rest implementation of a subset of Yelp dataset available at:
- [Yelp Open Dataset](https://www.yelp.com/dataset)
- [Yelp Subset](https://drive.google.com/file/d/1rPjOdKXggrs3QYcEk8MQ9yyAD_dPZPG9/view?usp=sharing)

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Yelp subset](https://drive.google.com/file/d/1rPjOdKXggrs3QYcEk8MQ9yyAD_dPZPG9/view?usp=sharing)

## Preinstallation

Before run any command follow the next steps:

Copy the file 'business10k.json' into the route: yelp -> business -> scripts

```bash
- yelp
| - api
| - business
| - - scripts
| - - - business10k.json
...
```
Then copy the file 'user100k.json' into the route: yelp -> user -> scripts
```bash
- yelp
| - api
| - business
...
| - user
| - - scripts
| - - - user100k.json
...
```
And finaly copy the file 'review1M.json' into the rout: yelp -> review -> scripts
```bash
- yelp
| - api
| - business
...
| - review
| - - scripts
| - - - review1M.json
...
```
## Installation

Create the containers and install all necesary dependencies to run the project:
```bash
  docker-compose up --build
```

Create all migrations:
```bash
  docker-compose run web python manage.py migrate
```

Load data, it's necessary execute the following commands in order:
```bash
  docker-compose run web python manage.py runscript load_business
  docker-compose run web python manage.py runscript load_users
  docker-compose run web python manage.py runscript load_reviews
```
The last one have taken about 20 minutes to load all registers.

Create a superuser and follow the instruction, remember you username and password, you will need it to authenticate:
```bash
  docker-compose run web python manage.py createsuperuser
```

Finally run the project:
```bash
  docker-compose up
```
## Components description

The project has three main apps:
- business
- review
- user
One for each model in the subset. This allows you to more easily scale the code and make it more readable.


## Running Tests

To run tests, run the following command

```bash
  docker-compose run web python manage.py test .
```

## Documentation
Swagger has been integrated, so if you want to know all the available endpoints, run the project and access to:

[http://localhost:8000/api/doc/](http://localhost:8000/api/doc/)

If you prefer to use Postman, I created this collection so you can play around with endpoints:

[Yelp Collecion](http://localhost:8000/api/doc/)

## Authors

- [@ArmandoVn](https://github.com/ArmandoVn)


## Related

Here are some intresting libraries:

- [Faker](https://faker.readthedocs.io/en/master/providers/faker.providers.python.html)
- [factory_boy](https://factoryboy.readthedocs.io/en/stable/introduction.html)
