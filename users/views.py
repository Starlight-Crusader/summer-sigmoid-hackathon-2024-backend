from rest_framework.views import APIView
from rest_framework import response, status
from rest_framework.decorators import api_view


from serializers import UserSerialzier


@api_view(['POST'])
def create_user(request):
    serializer = UserSerialzier(data=request.data)
    serializer.is_valid(raise_exception=True)

    if serializer.is_valid():
        user = serializer.save()
        user_data = UserSerializer(user).data

        return response.Response(
            {'user': user_data},
            status=status.HTTP_201_CREATED
        )
    else:
        return response.Response(
            {'message': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )