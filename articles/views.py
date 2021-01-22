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

        author = request.user

        response_data['author'] = author.username
        response_data['title'] = title
        response_data['description'] = description

        Article.objects.create(
            author=author,
            title = title,
            description = description,
            )
        return JsonResponse(response_data)

    return render(request, 'create_article.html', {'articles':articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'POST':
        comment_id = request.POST.get('comment_id')
        comm = request.POST.get('comm')

        if comment_id:
            Reply( user=request.user, 
            comm=comm, 
            comment = Comment.objects.get(id=int(comment_id))
            ).save()
        else:
            Comment(article=article, user=request.user, comm=comm).save()
        
    comments = []
    for c in Comment.objects.filter(article=article):
        comments.append([c, Reply.objects.filter(comment=c)])
    

    context = {
        'article': article,
        'comments': comments,
        'total_comments': article.comments.count(),
        # 'replies': comments.replies.all(),
    }
    return render(request, 'article_detail.html', context)