from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Article, Comment
from .forms import CommentForm
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
            title = title,
            description = description,
            )
        return JsonResponse(response_data)

    return render(request, 'create_article.html', {'articles':articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)

    comments = Comment.objects.filter(article=article)

    response_data = {}

    if request.POST.get('action') == 'post':
        name = request.POST.get('name')
        text = request.POST.get('text')

        response_data['name'] = name
        response_data['text'] = text

        Comment.objects.create(
            article=article,
            name=name,
            text=text,
            )
        return JsonResponse(response_data)

    context = {
        'article': article,
        'comments': comments,
    }
    return render(request, 'article_detail.html', context)
