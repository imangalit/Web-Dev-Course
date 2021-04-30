from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
        }
    def __str__(self):
        return f'{self.id} : {self.title}'


class Post(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Description')
    topic = models.ForeignKey(Topic,related_name="posts",on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} : {self.name} : {self.topic.to_json()}'

class Comment(models.Model):
    description = models.CharField(max_length=200, null=True)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.id} : {self.description}'

class Like(models.Model):
    count = models.FloatField(max_length=200, null=True)
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.id} : {self.count}'

class Dislike(models.Model):
    count = models.FloatField(max_length=200, null=True)
    post = models.ForeignKey(Post, related_name="dislikes", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.id} : {self.count}'
