from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:tt_slug>/', views.detail, name='detail'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.login, name='login')
]