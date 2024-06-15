from django.urls import path
from . import views


urlpatterns = [
    path('create', views.create_rating),
    path('get_by_pn', views.get_ratings_by_pn),
]   