from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    # Main page
    path('', views.index, name='index'),
    # List groups
    path('groups/<slug:slug>', views.group_posts, name='group_posts'),
]
