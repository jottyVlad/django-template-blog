from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Post(models.Model):

    title = models.CharField(
        max_length=255, default="Default title"
    )

    content = MarkdownxField(default="Default content")

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

    def get_update_url(self):
        return f"/{self.id}/update"

    def get_delete_url(self):
        return f"/{self.id}/delete"

    def formatted_markdown(self):
        return markdownify(self.content)

    def body_summary(self):
        return markdownify(self.content[:300] + '...')


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
