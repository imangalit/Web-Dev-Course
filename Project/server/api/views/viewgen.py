from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.models import Topic, Comment, Post
from api.serializer import TopicSerializer, CommentSerializer, PostSerializer

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def PostsTopicId(request, topic_id):
    if request.method == 'GET':
        categories = Post.objects.filter(topic_id = topic_id).order_by('-id')
        serializer = PostSerializer(categories, many=True)
        return Response(serializer.data)

class TopicListAPIView(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated]

class TopicDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated]

class CommentListAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
