import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import Http404
from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from django.views import View
from core.models import Topic,Post
from api.serializers import TopicSerializer, TopicSerializer2,PostSerializer, Post2Serializer


class TopicListAPIView(APIView):
    def get(self, request):
        topics = Topic.objects.filter(name__contains='5').order_by('-id')
        serializer = TopicSerializer2(topics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TopicSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TopicDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Topic.objects.get(id=pk)
        except Topic.DoesNotExist as e:
            raise Http404

    def get(self, request, pk=None):
        topic = self.get_object(pk)
        serializer = TopicSerializer2(topic)
        return Response(serializer.data)

    def put(self, request, pk=None):
        topic = self.get_object(pk)
        serializer = TopicSerializer2(instance=topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk=None):
        category = self.get_object(pk)
        category.delete()
        return Response({'message': 'deleted'}, status=204)

@api_view(['GET', 'POST'])
def topic_list(request):
    if request.method == 'GET':
        topics = Topic.objects.filter(name__contains='5').order_by('-id')
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TopicSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def topic_detail(request, topic_id):
    try:
        topic = Topic.objects.get(id=topic_id)
    except Topic.DoesNotExist as e:
        return Response({'message': str(e)}, status=400)

    if request.method == 'GET':
        serializer = TopicSerializer2(topic)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TopicSerializer2(instance=topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        topic.delete()
        return Response({'message': 'deleted'}, status=204)


class TopicListAPIView(mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          generics.GenericAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer2

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TopicDetailAPIView(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            generics.GenericAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer2
    # lookup_field = 'topic_id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class TopicListAPIView(generics.ListCreateAPIView):

    def get_queryset(self):
        return Topic.objects.all()
    # queryset = Topic.objects.all()
    serializer_class = TopicSerializer2
    permission_classes = (IsAuthenticated,)


class TopicDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer2


class PostListAPIView(generics.ListCreateAPIView):
    queryset =Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

@csrf_exempt
def topic_list(request):
    if request.method == 'GET':
        # topics = Topic.objects.filter(name='topic 5')
        # topics = Topic.objects.filter(name__startswith='cat')
        # topics = Topic.objects.filter(name__endswith='ed')
        # topics = Topic.objects.filter(name__contains='update')
        # topics = Topic.objects.filter(id__in=[1, 2, 3, 4])
        topics = Topic.objects.filter(title__contains='5').order_by('-id')
        topics_json = [topic.to_json() for topic in topics]
        return JsonResponse(topics_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            topic = Topic.objects.create(title=data['title'])
        except Exception as e:
            return JsonResponse({'message': str(e)})

        return JsonResponse(topic.to_json())


@csrf_exempt
def topic_detail(request, topic_id):
    try:
        topic = Topic.objects.get(id=topic_id)
    except Topic.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    if request.method == 'GET':
        return JsonResponse(topic.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        topic.title = data['title']
        topic.save()
        return JsonResponse(topic.to_json())
    elif request.method == 'DELETE':
        topic.delete()
        return JsonResponse({'message': 'deleted'}, status=204)

@csrf_exempt
def topic_list(request):
    if request.method == 'GET':
        topics = Topic.objects.filter(name__contains='5').order_by('-id')
        serializer = TopicSerializer2(topics, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = TopicSerializer2(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)


@csrf_exempt
def topic_detail(request, topic_id):
    try:
        topic = Topic.objects.get(id=topic_id)
    except Topic.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    if request.method == 'GET':
        serializer = TopicSerializer2(topic)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = TopicSerializer2(instance=topic, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({'message': 'deleted'}, status=204)