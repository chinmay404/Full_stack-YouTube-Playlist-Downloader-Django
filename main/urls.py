from django.contrib import admin
from django.urls import path
from main import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('',RedirectView.as_view(url='home', permanent=False), name='index'),
    path('home', views.home , name='about' ),
    path('about', views.about , name='about' ),
    path('contact', views.contact , name='contact' ),
    path('download_page', views.dowload_page , name='download_page' ),
    path('download/<str:q>', views.download , name='download' ),
    path('playlist', views.playlist , name='playlist' ),
    # path('status', views.staus , name='status' ),
]
