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

    category = models.ForeignKey('Category', default=None, null=True, on_delete=models.SET_NULL)

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


class Category(models.Model):
    name = models.CharField(max_length=128)
    category_rev = models.ForeignKey('self', on_delete=models.CASCADE, default=None, null=True, blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def get_post_categories(self, arr=None):
        if arr is None:
            arr = [self]

        if arr[-1].category_rev is not None:
            arr.append(arr[-1].category_rev)
            return self.get_post_categories(arr)

        list_categoris_str = ' >> '.join(list(map(str, arr[::-1])))
        return list_categoris_str
