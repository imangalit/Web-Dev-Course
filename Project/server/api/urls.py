from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token

from api.views import topic_list, topic_detail, TopicListAPIView, TopicDetailAPIView, \
    PostListAPIView, PostDetailAPIView

urlpatterns = [
    # path('topics/', topic_list),
    # path('topics/<int:topic_id>/', topic_detail)

    path('login/', obtain_jwt_token),

    path('topics/', TopicListAPIView.as_view()),
    path('topics/<int:pk>/', TopicDetailAPIView.as_view()),


    path('posts/', PostListAPIView.as_view()),
    path('posts/<int:pk>/', PostDetailAPIView.as_view())

]