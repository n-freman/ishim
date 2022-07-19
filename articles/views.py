from django.shortcuts import render
from .models import Article, ChosenArticle
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(('GET',))
def add_to_chosen(request, id):
    if not request.user:
        return Response(status=status.HTTP_404_NOT_FOUND)
    article = Article.objects.get(id=id)
    try:
        chosen = ChosenArticle.objects.get(
            user=request.user,
            article=article
        )
    except Exception:
        chosen = None
    if not chosen:
        print('[Creating]...')
        ChosenArticle.objects.create(
            user=request.user,
            article=article
        )
    else:
        print('[Deleting]...')
        chosen.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

class ArticleListView(ListView):
    model = Article
    ordering = ['-creation_date']


def article_detail(request, id):
    article = Article.objects.get(id=id)
    article.views += 1
    article.save()
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)


def favourite_articles(request):
    articles = [chosen.article for chosen in request.user.chosenarticle_set.all()]
    return articles