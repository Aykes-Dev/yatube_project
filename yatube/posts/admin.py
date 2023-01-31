from django.contrib import admin
from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    """View model Post in admin panel."""
    list_display = ('pk', 'text', 'pub_date', 'author', 'group',)
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    # Это свойство сработает для всех колонок:
    # где пусто — там будет эта строка
    empty_value_display = '-пусто-'


# Add model post in admin panel.
admin.site.register(Post, PostAdmin)
admin.site.register(Group)
