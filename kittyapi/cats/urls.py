from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import BreedViewSet, CatViewSet

router_v1 = DefaultRouter()

router_v1.register('cats',
                   CatViewSet,
                   basename='cats')
router_v1.register('breeds',
                   BreedViewSet,
                   basename='breeds')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/token/',
         TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
