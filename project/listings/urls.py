from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.listings,name='listings'),
    path('listone/',views.listone,name='listone'),
    path('search/',views.search,name='search'),
]