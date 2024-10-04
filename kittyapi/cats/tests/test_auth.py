from http import HTTPStatus

import pytest


@pytest.mark.django_db(transaction=True)
class TestAuth:

    url_create_user = '/api/v1/auth/users/'
    url_create_token = '/api/v1/auth/token/'

    def test_registation_user_valid_data(self, client):
        response = client.post(self.url_create_user, data={
            'username': 'qwerty123',
            'password': 'lxcvbnipf'
        })
        assert response.status_code == HTTPStatus.CREATED, (
            'Если все заполнено успешно, должны получить 201.'
        )

        response = client.post(self.url_create_token, data={
            'username': 'qwerty123',
            'password': 'lxcvbnipf'
        })
        assert response.status_code == HTTPStatus.OK, (
            'При правильных данных ответ должен быть 200'
        )

    def test_registation_user_invalid_data(self, client):
        response = client.post(self.url_create_user, data={
            'username': 'k233nfewj'
        })
        assert response.status_code == HTTPStatus.BAD_REQUEST, (
            'При отсуствии данных должен выдавать ошибку'
        )
