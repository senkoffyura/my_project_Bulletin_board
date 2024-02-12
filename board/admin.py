from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Author, Post, Comment


admin.site.register(Author)
admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Comment)

# Register your models here.
