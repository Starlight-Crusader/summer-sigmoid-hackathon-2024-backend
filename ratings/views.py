from rest_framework import response, status
from rest_framework.decorators import api_view
from .models import Rating
from products.models import Product
from .serializers import RatingSerializer, GetRatingSerializer, GetRatingsByProductSerializers
from users.models import User


def get_ratings_by_prod_name(prod_name):
    product = Product.objects.get(name=prod_name)
    return Rating.objects.filter(product=product)


@api_view(['GET'])
def get_reviews_by_name(request):
    serializer = GetRatingsByProductSerializers(data = request.data)
    serializer.is_valid(raise_exception=True)
    
    if serializer.is_valid():
        prod_name = serializer.validated_data.get("name")
        ratings = get_ratings_by_prod_name(prod_name)
        ratings_data = GetRatingSerializer(ratings, many = True).data
    
        return response.Response(
            {'ratings': ratings_data},
            status=status.HTTP_200_OK
        )
    else:
        return response.Response(
            {'message': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['POST'])
def create_rating(request):
    serialzier = RatingSerializer(data=request.data)
    serialzier.is_valid(raise_exception=True)

    if serialzier.is_valid():
        rating = serialzier.save()
        rating_data = GetRatingSerializer(rating).data

        return response.Response(
            {'new_rating': rating_data},
            status=status.HTTP_201_CREATED
        )
    else:
        return response.Response(
            {'message': serialzier.errors},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['POST'])
def recalc_avg(request, product_id):
    average = User.objects.get(username="Average")
    
    try:
        average_rating = Rating.objects.filter(product=product_id, author=average)
        average_rating.delete()
    except Rating.DoesNotExist:
        pass

    all_ratings = Rating.objects.all()
    authors = []

    for rating in all_ratings:
        authors.append(rating.author)

    pass