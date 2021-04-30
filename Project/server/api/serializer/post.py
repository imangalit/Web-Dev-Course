from rest_framework import serializers

from api.models import Post



class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    topic_id = serializers.IntegerField(read_only=True)

    def create(self, data):
        post = Post.objects.create(name=data.get('name'))
        return post

    def update(self, instance, data):
        instance.name = data.get('name')
        instance.description = data.get('description')
        instance.topic_id = data.get('topic_id')

        instance.save()
        return instance
