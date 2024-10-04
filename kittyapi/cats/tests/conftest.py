import pytest

from cats.models import Breed, Cat


@pytest.fixture
def Breed_1():
    return Breed.objects.create(name='Пушистый')


@pytest.fixture
def Breed_2():
    return Breed.objects.create(name='Лысый')


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(
        username='TestUser', password='1234567'
    )


@pytest.fixture
def user_2(django_user_model):
    return django_user_model.objects.create_user(
        username='TestUser2', password='1234567'
    )


@pytest.fixture
def token(user):
    from rest_framework_simplejwt.tokens import RefreshToken
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@pytest.fixture
def user_client(token):
    from rest_framework.test import APIClient

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token["access"]}')
    return client


@pytest.fixture
def Cat_1(Breed_1, user, user_2):
    return Cat.objects.create(name='Пушок',
                              description='Огромный',
                              age=9,
                              breed=Breed_1,
                              owner=user)


@pytest.fixture
def Cat_2(Breed_2, user, user_2):
    return Cat.objects.create(name='Анти Пушок',
                              description='Маленький',
                              age=9,
                              breed=Breed_2,
                              owner=user_2)
