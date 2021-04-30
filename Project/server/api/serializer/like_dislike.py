from rest_framework import serializers

from api.models import Like,Dislike


class LikeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    count = serializers.IntegerField(read_only=True)
    postid = serializers.IntegerField(read_only=True)

    def update(self, instance, data):
        instance.count = data.get('count')
        instance.save()
        return instance


class DislikeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    count = serializers.IntegerField(read_only=True)
    postid = serializers.IntegerField(read_only=True)

    def update(self, instance, data):
        instance.count = data.get('count')
        instance.save()
        return instance