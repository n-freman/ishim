from django.contrib import admin
from .models import Article, ChosenArticle

admin.site.register(Article)
admin.site.register(ChosenArticle)