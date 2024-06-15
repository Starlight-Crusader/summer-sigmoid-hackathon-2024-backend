from rest_framework import serializers
from .models import Rating
from users.serializers import UserSerializer
from products.serializers import GetProductSerializer


class RatingSerializer(serializers.ModelSerializer):
    values = serializers.ListField(
        child=serializers.IntegerField()
    )

    class Meta:
        model = Rating
        fields = '__all__'


class GetRatingSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    product = GetProductSerializer()

    class Meta:
        model = Rating
        fields = '__all__'


class GetRatingsByProductSerializers(serializers.Serializer):
    name = serializers.CharField()


class GetTinderCardsSerialzier(serializers.Serializer):
    parameters_priority = serializers.ListField(
        child=serializers.CharField()
    )