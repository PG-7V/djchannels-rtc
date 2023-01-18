from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import reverse
from django.utils import timezone

from utils.default_user import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Creator')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField()
    content = models.TextField(verbose_name='Содержимое поста')
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()
    comments = GenericRelation('comments.Comment')

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
