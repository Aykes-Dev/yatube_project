# from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    """Main page."""
    return HttpResponse('Main page.')


def group_posts(request):
    """Group."""
    return HttpResponse('Posts.')


def group_posts_detail(request, slug):
    """Group details."""
    return HttpResponse(f'Posts slug. {slug}')
