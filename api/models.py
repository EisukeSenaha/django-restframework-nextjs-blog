from django.db import models


class Post(models.Model):

    title = models.CharField('タイトル', max_length=50)
    content = models.CharField('コンテンツ', max_length=500)
    created_at = models.DateField('作成日', auto_now_add=True)

    def __str__(self):
        return str(self.id) + " - " + self.title



class Task(models.Model):

    title = models.CharField('タイトル', max_length=50)
    created_at = models.DateField('作成日', auto_now_add=True)

    def __str__(self):
        return str(self.id) + " - " + self.title

