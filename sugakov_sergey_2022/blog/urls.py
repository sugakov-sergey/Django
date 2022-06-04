from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_index),
    path("<int:pk>/", views.blog_detail, name='blog_detail_url'),
]
