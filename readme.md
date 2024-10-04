# Cat Management API
Этот проект — REST API для управления котами, их породами и рейтингами. Система позволяет пользователям управлять котами, присваивать им породы, а также оценивать котов. Проект реализован на базе Django и Django REST Framework (DRF).

## Функциональность

- Управление котами (создание, чтение, обновление, удаление)
- Управление породами котов
- Оценка котов пользователями (рейтинг от 1 до 5)
- Импорт данных из CSV файлов (коты, породы, пользователи, рейтинги)

## Технологии

- Python 3.11+
- Django 5.x
 - Django REST Framework
 - PostgreSQL (или любая другая база данных, поддерживаемая Django)
 - Docker (для контейнеризации)

## Установка

### Шаг 1: Клонирование репозитория
```
git clone https://github.com/yourusername/cat-management-api.git
cd cat-management-api
```
### Шаг 2: Как развернуть проект в Docker?


1. Перейдите в директорию проекта:
    ```bash
    cd menuapp
    ```

2. Запустите проект с помощью Docker Compose:
    ```bash
    sudo docker-compose up -d --build
    ```

3. Создайте суперпользователя для доступа к админке:
    ```bash
   python manage.py createsuperuser
    ```

## Импорт данных из CSV
В проекте предусмотрено автоматическое заполнение бд с помощью CSV файлов, находящихся в папке data, при желании их можно изменить и выполнить команду:
```
python manage.py import_data
```
## Тестирование
Для тестирования проекта используется pytest. Чтобы запустить тесты, используйте следующую команду:
```
pytest
```

API Endpoints
## Основные эндпоинты:
/api/v1/cats/ — управление, просмотр котиков
/api/v1/breeds/ — управление, просмотр пород
/api/v1/cats/{id}/rate/ — выставление рейтинга коту
/swagger
/api/v1/auth/user/

Запрос для регистрации
```
POST /api/v1/auth/user/
{
    'username': 'name',
    'password': 'strongpassword'
}
```

Запрос для получения токена 
```
POST /api/v1/auth/token/
{
    'username': 'name',
    'password': 'strongpassword'
}
```

Запрос для создания котика 
```
POST /api/v1/cats/
{
    'name': 'Афанасий',
    'age': 1,
    'breed': 'Сфинкс',
    'color': 'Черный',
}
```

Запрос для оценки кота:
```
POST /api/cats/{id}/rate/
{
  "rating": 5
}
```
