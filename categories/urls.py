from django.urls import path
from . import views


urlpatterns = [
    path('create', views.create_category),
    path('get_all', views.get_all_categories),
<<<<<<< HEAD
    path('get/<int:category_id>', views.get_category_by_id),
=======
>>>>>>> 092b038ed2d744222fe5523221c7c17475466a89
]   