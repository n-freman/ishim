from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='articles'),
    path('chosen/<id>', views.add_to_chosen, name='choose-article'),
    path('<int:id>', views.article_detail, name='article-detail'),
]