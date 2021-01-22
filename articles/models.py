from django.db import models
from django.contrib.auth.models import User,AbstractUser

# Custom User Model
class CustomUser(AbstractUser):
    bio=models.TextField()
    location=models.CharField(max_length=200)


class Article(models.Model):
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    title = models.CharField(max_length=160)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    comm = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.comm


class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    comm = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.comm


# UpVotes
class UpVote(models.Model):
    article=models.ForeignKey(Article, on_delete=models.CASCADE)
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='upvote_user')

# DownVotes
class DownVote(models.Model):
    article=models.ForeignKey(Article, on_delete=models.CASCADE)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='downvote_user')