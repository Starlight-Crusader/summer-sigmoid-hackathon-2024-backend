from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    parameters_list = serializers.ListField(
        child=serializers.CharField(max_length=40)
    )

    class Meta:
        model = Category
        fields = '__all__'