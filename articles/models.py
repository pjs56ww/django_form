from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk']   # 마지막에 생성된 친구가 가장 앞으로 올 수 있도록

    def __str__(self):
        return f'{self.pk} - {self.title}'
