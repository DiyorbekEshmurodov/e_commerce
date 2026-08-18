from django.db import models
from rest_framework import serializers
from .models import Product,Review,Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    avg_rating = serializers.FloatField(read_only=True,required=False)
    class Meta:
        model = Review
        fields = ['id','name','price','description','category','avg_rating']