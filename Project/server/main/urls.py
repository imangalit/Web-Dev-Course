from django.urls import path
from main.views import post_list, post_detail

urlpatterns = [
    path('posts/', post_list),
    path('posts/<int:post_id>/', post_detail)
]