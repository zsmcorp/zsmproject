from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:tt_slug>/', views.detail, name='detail'),
    path('search/', views.Search.as_view(), name='search ')
]