from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Post, Comment

admin.site.register(Post, MarkdownxModelAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass