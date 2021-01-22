from django.urls import path
from .views import home, create_article, article_detail


urlpatterns = [
    path('', home, name='home'),
    path('create_article/', create_article, name='create_article'),
    path('article/<int:pk>/', article_detail, name='article_detail'),
    # path('reply-comment/', reply_comment, name='reply-comment'),
]
