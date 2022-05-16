from django.urls import path
from . import views

urlpatterns = [
    path('',views.display,name='index'),
    path('about/',views.about,name='about'),
   
]
