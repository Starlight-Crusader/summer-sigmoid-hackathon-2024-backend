from django.urls import path
from . import views


urlpatterns = [
    path('create', views.create_rating),
    path('reviews', views.get_reviews_by_name),
]   