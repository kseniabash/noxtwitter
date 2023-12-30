from django.db import models
from django.conf import settings


class Post(models.Model):
    """ Пост """
    content = models.TextField(max_length=240,
                               null=False,
                               blank=False,
                               verbose_name='Содержимое')

    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                null=False,
                                on_delete=models.CASCADE,
                                related_name='posts',
                                verbose_name='Автор')

    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата создания')

    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                      related_name='liked_posts',
                                      verbose_name='Понравилось пользователям')

    def get_likes_count(self):
        return self.liked_by.count()

    class Meta:
        ordering = ('-created_at',)

        verbose_name = 'Пост'
        verbose_name_plural = 'посты'
