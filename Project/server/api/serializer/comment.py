from rest_framework import serializers

from api.models import Comment


class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField()
    post_id = serializers.IntegerField()

    def create(self, data):
        comment = Comment.objects.create(description=data.get('description'), post_id=data.get('post_id'))
        return comment

    def update(self, instance, data):
        instance.description = data.get['description']
        instance.post_id = data.get('post_id')
        instance.save()
        return instance