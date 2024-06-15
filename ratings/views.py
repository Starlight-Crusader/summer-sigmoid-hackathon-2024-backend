from rest_framework import response, status
from rest_framework.decorators import api_view
from .models import Rating
from .serializers import RatingSerializer


@api_view(['POST'])
def create_rating(request):
    pass