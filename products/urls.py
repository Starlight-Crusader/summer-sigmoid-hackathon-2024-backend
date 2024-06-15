from django.urls import path
from . import views


urlpatterns = [
    path('create', views.create_product),
    path('get', views.get_all_products),
    path('get/<int:product_id>', views.get_product_by_id),
    path('delete', views.delete_all_products),
    path('delete/<int:product_id>', views.delete_product_by_id)
]   