from django.urls import path
from . import views


urlpatterns = [
    path('create', views.create_rating),
    path('get_by_pn', views.get_ratings_by_pn),
    path('recalc-avg/<int:product_id>', views.recalc_avg),
    path('get-tc/<int:category_id>', views.get_tinder_cards),
    path('get-rr-by-cat', views.get_random_ratings_by_category)
]   