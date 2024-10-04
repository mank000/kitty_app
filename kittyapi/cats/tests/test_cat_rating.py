import pytest


@pytest.mark.django_db(transaction=True)
class TestCatsRating:

    url_cats = '/api/v1/cats/'

    def test_rate_another_cat(self, user_client, user_2, Cat_1, Cat_2):
        response = user_client.post(f'{self.url_cats}1/rate/', data={
            'rating': 5
        })
        print(response.json())
        assert response.json().get('Сообщение') == 'Учтено', (
            ('Правильный запрос на оценку '
             'котика возвращает не правильный статус')
        )

    def test_rate_with_bad_number(self, user_client, user_2, Cat_1, Cat_2):
        response = user_client.post(f'{self.url_cats}1/rate/', data={
            'rating': 66
        })
        print(response.json())
        assert response.json().get('rating')[0] == ('Убедитесь, что '
                                                    'это значение меньше '
                                                    'либо равно 5.'), (
            ('Правильный запрос на оценку котика '
             'возвращает не правильный статус')
        )
