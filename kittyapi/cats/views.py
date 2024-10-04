from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .filters import CatFilter
from .models import Breed, Cat
from .permissions import OwnerOrReadOnly
from .serializators import (BreedSerilizer, CatSerializer, FullCatSerializer,
                            RatingSerializer)


class CatViewSet(viewsets.ModelViewSet):

    queryset = Cat.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CatFilter
    permission_classes = (OwnerOrReadOnly,)

    @action(detail=True, methods=['POST'], url_path='rate')
    def rate_cat(self, request, pk=None):

        self.permission_classes = (permissions.IsAuthenticated,)

        serializer = RatingSerializer(
            data=request.data, context={'request': request, 'pk': pk})

        if serializer.is_valid():
            serializer.save()
            return Response({"Сообщение": "Учтено"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        if self.action == 'list':
            return CatSerializer
        return FullCatSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BreedViewSet(viewsets.ModelViewSet):

    queryset = Breed.objects.all()
    serializer_class = BreedSerilizer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
