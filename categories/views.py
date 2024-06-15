from rest_framework import response, status
from rest_framework.decorators import api_view
from serializers import CategorySerializer


api_view(['DELETE'])
def create_category(request):
    serializer = CategorySerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    if serializer.is_valid():
        category = serializer.save()
        category_data = CategorySerializer(category).data

        return response.Response(
            {'new_category': category_data},
            status=status.HTTP_201_CREATED
        )
    else:
        return response.Response(
            {'message': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )