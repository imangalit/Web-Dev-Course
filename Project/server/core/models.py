from django.db import models

class Topic(models.Model):
    title = models.CharField(max_length=200,verbose_name='Название')

    class Meta:
        verbose_name = "Топик"
        verbose_name_plural = "Топики"
    
    def to_json(self):
        return {
            'id': self.id,
            'title': self.title
        }
    
    def __str__(self):
        return f"{self.title}"

class Post(models.Model):
    name = models.CharField(max_length=200,verbose_name='Название')
    description = models.TextField(verbose_name='Description')
    topic = models.ForeignKey(Topic,related_name="posts",on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
    
    def __str__(self):
        return f'{self.id}: {self.name} | {self.description}'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }
    
