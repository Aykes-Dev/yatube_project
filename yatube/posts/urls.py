from django.urls import path
from . import views


urlpatterns = [
    # Main page
    path('', views.index),
    # List groups
    path('groups/', views.group_posts),
    # View simple post
    path('groups/<slug:slug>/', views.group_posts_detail),
]
