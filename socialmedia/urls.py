from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.userlogin, name = 'login'),
    path('logout/', views.userlogout, name = 'ulogout'),
    path('register/', views.register, name = 'register'),

    path('', views.home, name='home'),
    path('userProfile/<str:pk>/', views.userProfile, name = 'useraccount')
]