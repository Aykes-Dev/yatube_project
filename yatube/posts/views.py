from django.shortcuts import render, get_object_or_404
from .models import Post, Group


# Create your views here.
def index(request):
    """Main page."""
    title = 'Это главная страница проекта Yatube'
    posts = Post.objects.order_by('-pub_date')[:10]
    content = {'title': title,
               'posts': posts}
    return render(request, 'posts/index.html', content)


def group_posts(request, slug):
    """Group."""
    title = 'Здесь будет информация о группах проекта Yatube'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    content = {'group': group,
               'posts': posts,
               'title': title}
    return render(request, 'posts/group_list.html', content)
