from rest_framework.decorators import api_view
from rest_framework import response, status
from .serializers import ProductSerializer


@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    if serializer.is_valid():
        product = serializer.save()
        product_data = ProductSerializer(product).data

        return response.Response(
            {'new_product': product_data},
            status=status.HTTP_201_CREATED
        )
    else:
        return response.Response(
            {'message': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )