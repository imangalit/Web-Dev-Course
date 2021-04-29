from rest_framework import serializers

from core.models import Topic, Post


class TopicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()

    def create(self, validated_data):
        topic = Topic.objects.create(title=validated_data['title'])
        return topic

    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.save()
        return instance


class Post2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'name', 'description')


class TopicSerializer2(serializers.ModelSerializer):
    title = serializers.CharField()

    # Posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # Posts = serializers.StringRelat    edField(many=True, read_only=True)

    # Posts = Post2Serializer(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = ('id', 'title',)
        # read_only_fields = ('name',)


class PostSerializer(serializers.ModelSerializer):
    topic = TopicSerializer2(read_only=True)
    topic_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Post
        fields = ('id', 'name', 'description', 'topic', 'topic_id',)