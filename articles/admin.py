from django.contrib import admin

from .models import Article, Comment, Reply

admin.site.register(Article)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'comment_text', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user', 'comment_text')


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('comment', 'reply_text', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user', 'reply_text')