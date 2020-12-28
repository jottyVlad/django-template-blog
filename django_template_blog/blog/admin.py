from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Post, Comment, Category

admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Comment)
admin.site.register(Category)