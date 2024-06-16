from rest_framework import response, status
from rest_framework.decorators import api_view
from .models import Rating
from products.models import Product
from .serializers import RatingSerializer, GetRatingSerializer, GetRatingsByProductSerializers, GetTinderCardsSerialzier, GetAvgsByIdsSerialzier
from users.models import User
from categories.models import Category


def search_ratings_by_prod_name(prod_name):
    product = Product.objects.get(name=prod_name)
    return Rating.objects.filter(product=product)


@api_view(['POST'])
def get_ratings_by_pn(request):
    serializer = GetRatingsByProductSerializers(data = request.data)
    serializer.is_valid(raise_exception=True)
    
    if serializer.is_valid():
        prod_name = serializer.validated_data.get("name")
        ratings = search_ratings_by_prod_name(prod_name)
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
        try:
            rating = Rating.objects.get(author=serialzier.validated_data.get("author"), product=serialzier.validated_data.get("product"))

            return response.Response(
                {'message': "You are not allowed to create another review!"},
                status=status.HTTP_403_FORBIDDEN
            )
        except Rating.DoesNotExist:
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
    average = User.objects.get(username="KidNamedAverage")
    
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return response.Response(
            {'message': "Product not found!"},
            status=status.HTTP_404_NOT_FOUND
        )

    try:
        average_rating = Rating.objects.filter(product=product, author=average)
        average_rating.delete()
    except Rating.DoesNotExist:
        pass

    ratings = list(Rating.objects.filter(product=product))
    authors = []

    for rating in ratings:
        authors.append(rating.author)

    overall_score = 0
    for author in authors:
        overall_score += max(0, author.score + 1)

    weights = []
    for author in authors:
        weights.append((author.score + 1) / overall_score)

    category = product.category
    parameters = category.parameters_list

    average_rating = Rating.objects.create(author=User.objects.get(username="KidNamedAverage"), product=product, values=[0, 0, 0, 0, 0])

    for param_idx in range(len(parameters)):
        for rating_idx in range(len(ratings)):
            average_rating.values[param_idx] += ratings[rating_idx].values[param_idx] * weights[rating_idx]
    
    average_rating.save()
    average_rating_data = GetRatingSerializer(average_rating).data

    return response.Response(
        {'average_rating': average_rating_data},
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
def get_tinder_cards(request, category_id):
    serializer = GetTinderCardsSerialzier(data=request.data)
    serializer.is_valid(raise_exception=True)

    if serializer.is_valid():
        category = None
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return response.Response(
                {'message': "Category not found!"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        parameters_priority = serializer.validated_data.get("parameters_priority")
        original_parameters = category.parameters_list

        original_param_idxs = []
        for param_idx in range(len(parameters_priority)):
            original_param_idxs.append(original_parameters.index(parameters_priority[param_idx]))

        priority_sum = 0
        for i in range(1, len(parameters_priority) + 1):
            priority_sum += i

        weights = []
        for param_idx in range(len(parameters_priority)):
            weights.append((len(parameters_priority) - param_idx) / priority_sum)

        products = list(Product.objects.filter(category=category))
        avg_author = User.objects.get(username="KidNamedAverage")

        card_pool = []
        for product in products:
            avg_rating = Rating.objects.get(product=product, author=avg_author)

            fin_score = 0
            for idx in range(len(weights)):
                fin_score += avg_rating.values[original_param_idxs[idx]] * weights[idx]

            card_pool.append([product.id, fin_score])

        for i in range(len(card_pool)):
            for j in range(len(card_pool)-i-1):
                if (card_pool[j][1] < card_pool[j+1][1]):
                    card_pool[j], card_pool[j+1] = card_pool[j+1], card_pool[j]

        card_pool = card_pool[:10]

        res_data = []
        for card in card_pool:
            res_data.append(Rating.objects.get(author=avg_author, product=Product.objects.get(id=card[0])))

        res_data = GetRatingSerializer(res_data, many=True).data

        return response.Response(
            {'cards': res_data},
            status=status.HTTP_200_OK
        )
    else:
        return response.Response(
            {'message': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
    

@api_view(['GET'])
def get_random_ratings_by_category(request, category_id):
    category = None
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return response.Response(
            {'message': "Category does not exist!"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    avg_author = User.objects.get(username="KidNamedAverage")
    products_in_category = Product.objects.filter(category=category)
    ratings = Rating.objects.filter(product__in=products_in_category, author=avg_author)
    ratings_data = GetRatingSerializer(ratings, many=True).data

    return response.Response(
        {'ratings_data': ratings_data},
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
def get_avg_by_ids(request):
    serialzier = GetAvgsByIdsSerialzier(data=request.data)
    serialzier.is_valid(raise_exception=True)

    if serialzier.is_valid():
        ids = serialzier.validated_data.get("ids")
        products = Product.objects.filter(id__in=ids)
        ratings = Rating.objects.filter(author=User.objects.get(username="KidNamedAverage"), product__in=products)
        ratings_data = GetRatingSerializer(ratings, many=True).data

        return response.Response(
            {'ratings_data': ratings_data},
            status=status.HTTP_200_OK
        )
    else:
        return response.Response(
            {'message': serialzier.errors},
            status=status.HTTP_400_BAD_REQUEST
        )