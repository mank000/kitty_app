from http import HTTPStatus

import pytest


@pytest.mark.django_db(transaction=True)
class TestBreeds:

    url = '/api/v1/breeds/'

    def test_watch_breeds(self, client, Breed_1, Breed_2):
        response = client.get(self.url)
        ans = response.json()
        assert ans.get('count') == 2, (
            'Вывод всех пород работает не правильно'
        )

        assert ans.get('results')[0].get('name') == 'Пушистый', (
            'Отсутствует правильный вывод'
        )

    def test_creating_breeds(self, user_client):

        response = user_client.post(self.url, data={
            'name': 'Сиамская'
        })

        assert response.status_code == HTTPStatus.CREATED, (
            'Получен не правильный статус код'
        )
