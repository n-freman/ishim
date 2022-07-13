from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    image = models.ImageField(default='article_default.jpg', upload_to='article_images')
    title = models.CharField(max_length=130)
    content = models.TextField()
    views = models.IntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ChosenArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}: {self.article.title}'