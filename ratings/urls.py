from django.urls import path
from . import views


urlpatterns = [
    path('create', views.create_rating),
<<<<<<< HEAD
    path('reviews', views.get_reviews_by_name),
=======
    path('get_by_pn', views.get_ratings_by_pn),
>>>>>>> 707db7fc320afc4fa404ec76235192db3db881d1
]   