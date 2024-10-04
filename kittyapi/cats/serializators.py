from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Breed, Cat, CatRating

User = get_user_model()


class BreedSerilizer(serializers.ModelSerializer):
    """Класс сериализатора для отображения пород"""

    class Meta:
        model = Breed
        fields = ['id', 'name']


class CatSerializer(serializers.ModelSerializer):
    """Класс сериализатора для отображения не полной информции о котике."""
    breed = serializers.StringRelatedField(read_only=True)
    my_rate = serializers.SerializerMethodField()

    class Meta:
        model = Cat
        fields = ['id', 'name', 'breed', 'my_rate']

    def get_my_rate(self, obj):
        """
        Возвращает рейтинг, который поставил текущий пользователь, если есть.
        """
        user = self.context['request'].user
        if not user.is_authenticated:
            return None
        rating = obj.ratings.filter(user=user).first()
        return rating.rating if rating else None


class FullCatSerializer(serializers.ModelSerializer):
    """Класс сериализатора для отображения полной информации о котике."""
    breed = serializers.CharField(required=True)
    owner = serializers.SlugRelatedField(slug_field='username', read_only=True)
    my_rate = serializers.SerializerMethodField()

    class Meta:
        model = Cat
        fields = ['id', 'name', 'breed', 'age', 'description', 'owner',
                  'my_rate']

    def get_my_rate(self, obj):
        """
        Возвращает рейтинг, который поставил текущий пользователь, если есть.
        """
        user = self.context['request'].user
        if not user.is_authenticated:
            return None
        rating = obj.ratings.filter(user=user).first()
        return rating.rating if rating else None

    def create(self, validated_data):
        breed_name = validated_data.pop('breed')
        breed, created = Breed.objects.get_or_create(name=breed_name)
        cat = Cat.objects.create(breed=breed, **validated_data)
        return cat

    def update(self, instance, validated_data):
        breed_name = validated_data.pop('breed', None)

        if breed_name:
            breed, created = Breed.objects.get_or_create(name=breed_name)
            instance.breed = breed
            return super().update(instance, validated_data)
        return super().update(instance, validated_data)


class RatingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = CatRating
        fields = ['rating']

    def create(self, validated_data):

        user = self.context['request'].user
        if not user.is_authenticated:
            return None

        rating, created = CatRating.objects.update_or_create(
            user=user,
            cat_id=self.context['pk'],
            rating=validated_data.pop('rating')
        )
        return rating
