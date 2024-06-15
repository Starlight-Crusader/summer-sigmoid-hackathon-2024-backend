from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create_user),
    path('drop', views.delete_all_users),
    path('drop/<int:user_id>', views.delete_user_by_id),
]