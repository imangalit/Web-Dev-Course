from django.contrib import admin
from api.models import Topic,Post,Comment,Like,Dislike

# Register your models here.
admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Dislike)