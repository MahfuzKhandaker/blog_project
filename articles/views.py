from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Article, Comment, Reply
from django.contrib import messages


def home(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'home.html', context)

def create_article(request):
    articles = Article.objects.all()
    response_data = {}

    if request.POST.get('action') == 'post':
        title = request.POST.get('title')
        description = request.POST.get('description')

        response_data['title'] = title
        response_data['description'] = description

        Article.objects.create(
            author=request.user,
            title = title,
            description = description,
            )
        return JsonResponse(response_data)

    return render(request, 'create_article.html', {'articles':articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)

    comments = Comment.objects.filter(article=article)

    # replies = Reply.objects.filter(comment=Comment.objects.get(pk=pk))

    response_data = {}

    # Comment Section
    if request.POST.get('action') == 'post':
        comment_text = request.POST.get('comment_text')
        user=request.user
        response_data['comment_text'] = comment_text
        response_data['user'] = user.username

        Comment.objects.create(
            article=article,
            user=user,
            comment_text=comment_text,
            )

        # An HTTP response class that consumes data to be serialized to JSON.
        return JsonResponse(response_data)

    context = {
        'article': article,
        'comments': comments,
        # 'replies': comments.replies.all(),
    }
    return render(request, 'article_detail.html', context)


def reply_comment(request):
    if request.method=='POST':
        comment_id=request.POST['comment_id']
        comment=Comment.objects.get(pk=comment_id)
        reply_text = request.POST['reply_text']
        

        Reply.objects.create(
            comment=comment,
            user=request.user,
            reply_text=reply_text,
        )
        return JsonResponse({'bool':True})