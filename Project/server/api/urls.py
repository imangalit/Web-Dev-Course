from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from api.views import *

urlpatterns = [
    path('topics/', TopicListAPIView.as_view()),
    path('topics/<int:pk>', TopicDetailAPIView.as_view()),
    path('comments/', CommentListAPIView.as_view()),
    path('login/', obtain_jwt_token),
    path('posts/', PostListAPIView.as_view()),
    path('posts/<int:pk>/', PostDetailAPIView.as_view()),

    path('postsTopicId/<int:topic_id>/', PostsTopicId),
    path('commentsPostId/<int:post_id>/', CommentsPostId),

]