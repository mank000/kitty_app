import django_filters

from .models import Cat


class CatFilter(django_filters.FilterSet):
    breed = django_filters.CharFilter(
        field_name='breed__name', lookup_expr='iexact')

    class Meta:
        model = Cat
        fields = ['breed']
