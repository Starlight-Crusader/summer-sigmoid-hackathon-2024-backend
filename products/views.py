from rest_framework.decorators import api_view
from rest_framework import response, status
from .serializers import ProductSerializer, GetProductSerializer
from .models import Product


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


@api_view(['GET'])
def get_all_products(request):
    products = Product.objects.all()
    serializer = GetProductSerializer(products, many=True)
    
    return response.Response(
        {'products': serializer.data},
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
def get_product_by_id(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        serializer = GetProductSerializer(product)
        
        return response.Response(
            {'product': serializer.data},
            status=status.HTTP_200_OK
        )
    except Product.DoesNotExist:
        return response.Response(
            {'message': 'Product not found.'},
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(['DELETE'])
def delete_all_products(request):
    products = Product.objects.all()
    products.delete()
    
    return response.Response(
        {'message': 'All products have been deleted.'},
        status=status.HTTP_204_NO_CONTENT
    )


@api_view(['DELETE'])
def delete_product_by_id(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        
        return response.Response(
            {'message': f'Product with id {product_id} has been deleted.'},
            status=status.HTTP_204_NO_CONTENT
        )
    except Product.DoesNotExist:
        return response.Response(
            {'message': 'Product not found.'},
            status=status.HTTP_404_NOT_FOUND
        )