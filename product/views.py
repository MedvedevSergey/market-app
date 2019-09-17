from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import BaseFilterBackend

from .serializers import ProductSerializer, CategorySerializer, CharacteristicSerializer
from .models import Product, Category, Characteristic


class IsOwnerFilterBackend(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        category = request.GET.get('category')
        if category is not None:
            category_qs = Category.objects.get(id=category).get_descendants(include_self=True)
            return Product.objects.filter(category__in=category_qs)
        return queryset


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend, IsOwnerFilterBackend]
    filterset_fields = ['category', 'characteristics', 'price', 'rating']

    @action(detail=True, methods=['get'])
    def characteristics(self, request, *args, **kwargs):
        product = self.get_object()
        characteristic_qs = Characteristic.objects.filter(product=product)
        serializer = CharacteristicSerializer(characteristic_qs, context=self.get_serializer_context(), many=True)
        return Response(serializer.data)


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    @action(detail=True, methods=['get'])
    def products(self, request, *args, **kwargs):
        category = self.get_object()
        product_qs = Product.objects.filter(category=category)
        serializer = ProductSerializer(product_qs, context=self.get_serializer_context(), many=True)
        return Response(serializer.data)
