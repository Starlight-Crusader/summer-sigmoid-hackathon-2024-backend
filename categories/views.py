from rest_framework import response, status
from rest_framework.decorators import api_view
from .serializers import CategorySerializer
from .models import Category
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['POST'])
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


@api_view(['GET'])
def get_all_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    
    return response.Response(
        {'categories': serializer.data},
        status=status.HTTP_200_OK
    )

@api_view(['GET'])
def get_category_by_id(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
        serializer = CategorySerializer(category)
        return response.Response(
            {'category': serializer.data},
            status=status.HTTP_200_OK
        )
    except Category.DoesNotExist:
        return response.Response(
            {'message': 'Category not found.'},
            status=status.HTTP_404_NOT_FOUND
        )
    
@api_view(['DELETE'])
def delete_all_categories(request):
    categories = Category.objects.all()
    categories.delete()
    
    return response.Response(
        {'message': 'All categories have been deleted.'},
        status=status.HTTP_204_NO_CONTENT
    )

@api_view(['DELETE'])
def delete_category_by_id(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
        category.delete()
        return response.Response(
            {'message': f'Category with id {category_id} has been deleted.'},
            status=status.HTTP_204_NO_CONTENT
        )
    except Category.DoesNotExist:
        return response.Response(
            {'message': 'Category not found.'},
            status=status.HTTP_404_NOT_FOUND
        )