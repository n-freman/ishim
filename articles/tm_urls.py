from django.urls import path
from . import tm_views

urlpatterns = [
    path('', tm_views.ArticleListView.as_view(), name='articles-tm'),
    path('chosen/<id>', tm_views.add_to_chosen, name='choose-article-tm'),
    path('<int:id>', tm_views.article_detail, name='article-detail-tm'),
]