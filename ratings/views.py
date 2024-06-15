from rest_framework import response, status
from rest_framework.decorators import api_view
from .models import Rating
from products.models import Product
from .serializers import RatingSerializer, GetRatingSerializer


def get_ratings_by_prod_name(prod_name):
    product = Product.objects.get(name=prod_name)
    prod_id = product.id

    return Rating.objects.get(product=prod_id)


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