import csv
import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from cats.models import Cat, CatRating, Breed


class Command(BaseCommand):
    help = 'Импорт данных из CSV файлов в базу данных'

    def handle(self, *args, **kwargs):
        base_dir = os.path.join('/app/data')

        # Импорт пользователей
        self.import_users(os.path.join(base_dir, 'users.csv'))

        # Импорт пород котов
        self.import_breeds(os.path.join(base_dir, 'breed.csv'))

        # Импорт котов
        self.import_cats(os.path.join(base_dir, 'cat.csv'))

        # Импорт рейтингов котов
        self.import_ratings(os.path.join(base_dir, 'catrate.csv'))

        self.stdout.write(
            self.style.SUCCESS('Все данные успешно импортированы!'))

    def import_users(self, csv_file_path):
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(
                csv_file, delimiter=',',
                fieldnames=[
                    'id',
                    'password',
                    'username',
                    'is_superuser',
                    'last_login',
                    'last_name',
                    'email',
                    'is_staff',
                    'is_active',
                    'date_joined',
                    'first_name'])

            for row in csv_reader:
                try:
                    User.objects.create_user(
                        username=row['username'],
                        email=row['email'],
                        password=row['password']
                    )
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(
                            f'Ошибка при сохранении пользователя: {e}')
                    )

    def import_breeds(self, csv_file_path):
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(
                csv_file, delimiter=',', fieldnames=['id', 'name'])

            for row in csv_reader:
                try:
                    Breed.objects.create(name=row['name'])
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f'Ошибка при сохранении породы: {e}')
                    )

    def import_cats(self, csv_file_path):
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(
                csv_file, delimiter=',', fieldnames=[
                    'id',
                    'name', 'description', 'age', 'breed', 'color', 'owner'])

            for row in csv_reader:
                try:
                    breed = Breed.objects.filter(id=row['breed']).first()
                    owner = User.objects.filter(id=row['owner']).first()

                    Cat.objects.create(
                        name=row['name'],
                        age=row['age'],
                        breed=breed,
                        owner=owner,
                        color=row['color'],
                        description=row['description']
                    )
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f'Ошибка при сохранении кота: {e}')
                    )

    def import_ratings(self, csv_file_path):
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(
                csv_file, delimiter=',',
                fieldnames=['id', 'rating', 'user_id', 'cat_id'])

            for row in csv_reader:
                try:
                    cat = Cat.objects.filter(id=row['cat_id']).first()
                    user = User.objects.filter(id=row['user_id']).first()

                    CatRating.objects.create(
                        cat=cat,
                        user=user,
                        rating=row['rating']
                    )
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(
                            f'Ошибка при сохранении рейтинга: {e}')
                    )
