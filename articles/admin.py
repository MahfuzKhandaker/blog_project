from django.contrib import admin

from .models import Article, Comment

admin.site.register(Article)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'name', 'text', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'text')
