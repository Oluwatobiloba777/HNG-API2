from django.urls import path
from . import views

urlpatterns = [
    path('', views.user, name='user'),
    path('<int:pk>/', views.user_details, name='user_details'),  
]