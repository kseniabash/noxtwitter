from django.contrib import admin

from noxtwitter import models


@admin.register(models.Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'get_likes_count', 'creator']
    search_fields = ['content', 'creator__username']
    autocomplete_fields = ['creator', 'liked_by']
