from django.urls import path
from . import views


urlpatterns = [
    path('create', views.create_category),
    path('get_all', views.get_all_categories),
]   