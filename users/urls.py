from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create_user),
    path('drop', views.),
    path('drop/<int:user_id>', TokenRefreshView.as_view(), name='token_refresh'),
]