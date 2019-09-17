from rest_framework.fields import ListField
from rest_framework.serializers import ModelSerializer
from rest_framework_recursive.fields import RecursiveField
from .models import Product, Category, Characteristic, CharacteristicType


class CategorySerializer(ModelSerializer):
    parent = ListField(read_only=True, source='get_ancestors', child=RecursiveField())

    class Meta:
        model = Category
        fields = ['id', 'title', 'parent']


class ProductSerializer(ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'


class CharacteristicSerializer(ModelSerializer):

    class Meta:
        model = Characteristic
        fields = '__all__'


class CharacteristicTypeSerializer(ModelSerializer):
    class Meta:
        model = CharacteristicType
        fields = '__all__'
