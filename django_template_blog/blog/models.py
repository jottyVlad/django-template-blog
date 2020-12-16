from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):

    title = models.CharField(
        max_length=255, default="Default title"
    )

    content = models.TextField(default="Default content")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_published = models.BooleanField(default=False)

    author = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/posts/{self.id}"

