from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone

from utils.default_user import User


class Comment(models.Model):
    author = models.ForeignKey(User, verbose_name='Автор комментария', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    text = models.TextField(verbose_name='Текст комментария')
    created_at = models.DateTimeField(editable=False)

    def __str__(self):
        return f"{self.id}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        super().save(*args, **kwargs)
