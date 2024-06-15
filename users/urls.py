from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create_user),
    path('drop', views.delete_all_users),
    path('drop/<int:user_id>', views.delete_user_by_id),
<<<<<<< HEAD
    path('users/increment/<int:user_id>/', views.increment_value),
    path('users/decrement/<int:user_id>/', views.decrement_value),
=======
    path('inc/<int:user_id>', views.increment_value),
    path('dec/<int:user_id>', views.decrement_value),
>>>>>>> da2f18e4f2755f647f0d799ce64e9d1a1a97b589
]