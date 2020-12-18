from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    title = models.CharField(
        max_length=255, default="Default title"
    )

    content = models.TextField(default="Default content")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    views = models.IntegerField(default=0)

    is_published = models.BooleanField(default=False)

    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        unique=False,
        null=True,
        default=None
    )

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/{self.id}"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=False)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.post.title
