from rest_framework import serializers

from api.models import Comment


class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    description = serializers.CharField()
    postid = serializers.IntegerField()

    def create(self, data):
        comment = Comment.objects.create(description=data.get(['description']))
        return comment

    def update(self, instance, data):
        instance.description = data.get['description']
        instance.save()
        return instance