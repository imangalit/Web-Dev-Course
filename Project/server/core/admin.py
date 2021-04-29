from django.contrib import admin
from .models import Topic,Post

@admin.register(Topic)
class Topic(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ['name','description']
