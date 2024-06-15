from django.urls import path
from . import views


urlpatterns = [
    path('create', views.create_category),
    path('get_all', views.get_all_categories),
    path('get/<int:category_id>', views.get_category_by_id),
    path('delete', views.delete_all_categories),
    path('delete/<int:category_id>', views.delete_category_by_id),
]   