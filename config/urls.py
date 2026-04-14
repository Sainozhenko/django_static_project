from django.urls import path
from static_pages_1 import views

urlpatterns = [
    path('', views.home),
    path('contact/', views.contact),
    path('about/', views.about),
    path('store/', views.store),
]
