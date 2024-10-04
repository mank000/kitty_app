from django.contrib import admin

from .models import Breed, Cat, CatRating

admin.site.empty_value_display = '(None)'

admin.site.register(Cat)
admin.site.register(CatRating)
admin.site.register(Breed)
