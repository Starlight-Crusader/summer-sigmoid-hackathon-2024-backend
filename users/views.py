from rest_framework import response, status
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer


@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    if serializer.is_valid():
        user = serializer.save()
        user_data = UserSerializer(user).data

        return response.Response(
            {'new_user': user_data},
            status=status.HTTP_201_CREATED
        )
    else:
        return response.Response(
            {'message': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['DELETE'])
def delete_all_users(request):

    User.objects.all().delete()
    
    return response.Response(
        {'message': 'All users have been deleted.'},
        status=status.HTTP_200_OK
    )


@api_view(['DELETE'])
def delete_user_by_id(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return response.Response(
            {'message': f'User with id {user_id} has been deleted.'},
            status=status.HTTP_200_OK
        )
    except User.DoesNotExist:
        return response.Response(
            {'message': 'User not found.'},
            status=status.HTTP_404_NOT_FOUND
        )