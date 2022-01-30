from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    content = models.TextField(max_length=1000, verbose_name='Описание')
    date_posted = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    likes = models.IntegerField(default=0, verbose_name='Лайки')
    dislikes = models.IntegerField(default=0, verbose_name='Дислайки')

    def __str__(self):
        return self.content[:5]

    @property
    def number_of_comments(self):
        return Comment.objects.filter(post_connected=self).count()

    class Meta:
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    content = models.TextField(max_length=150, verbose_name='Описание')
    date_posted = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    post_connected = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'


class Preference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
    value = models.IntegerField(verbose_name='Количество')
    date = models.DateTimeField(auto_now = True, verbose_name='Дата')

    def __str__(self):
        return str(self.user) + ':' + str(self.post) + ':' + str(self.value)

    class Meta:
        verbose_name = 'Люди'
        verbose_name_plural = 'Люди'
        unique_together = ("user", "post", "value")
