from rest_framework import response, status
from rest_framework.decorators import api_view
from .models import Rating
from .serializers import RatingSerializer, GetRatingsByProductSerializers



@api_view(['POST'])
def create_rating(request):
    pass

@api_view(['GET'])
def get_reviews_by_name(request):
    serializer = GetRatingsByProductSerializers
    try:
        
        name = request.query_params.get('name', None)
        if not name:
            return response.Response(
                {'message': 'Name parameter is required in the query string.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        reviews = Rating.objects.filter(name=name)
        serializer = RatingSerializer(reviews, many=True)
        
        return response.Response(
            {'reviews': serializer.data},
            status=status.HTTP_200_OK
        )
    except Exception as e:
        return response.Response(
            {'message': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )