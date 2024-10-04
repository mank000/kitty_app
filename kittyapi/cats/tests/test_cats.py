from http import HTTPStatus

import pytest


@pytest.mark.django_db(transaction=True)
class TestCats:

    url_cats = '/api/v1/cats/'

    def test_see_cats(self, client, Cat_1, Cat_2):
        response = client.get(self.url_cats)
        ans = response.json()
        print(ans)
        assert ans.get('count') == 2, (
            'Неверное отображение кол-ва котиков'
        )

    def test_create_cat(self, user_client):
        response = user_client.post(self.url_cats, data={
            'name': 'Кирюша',
            'age': 12,
            'breed': 'Британец'
        })
        assert response.status_code == HTTPStatus.CREATED, (
            'При создании котика статус код должен быть 200'
        )

    def test_edit_another_cat(self, user_client, Cat_2):
        response = user_client.patch(f'{self.url_cats}{Cat_2.id}/', data={
            'name': 'Измененное имя'
        })

        assert response.status_code == HTTPStatus.FORBIDDEN, (
            'При изменении чужого котика должен быть код 403'
        )

    def test_edit_my_cat(self, user_client, Cat_1):
        response = user_client.patch(f'{self.url_cats}{Cat_1.id}/', data={
            'name': 'Измененное имя'
        })

        assert response.status_code == HTTPStatus.OK, (
            'При изменении моего котика должен быть код 200'
        )
