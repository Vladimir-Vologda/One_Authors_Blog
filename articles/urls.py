from django.urls import path

from articles.views import (
    ListArticleView, DetailArticleView, CreateArticleView
)

urlpatterns = [
    path('', ListArticleView.as_view(), name='list_article'),
    path('article/<slug:slug>/', DetailArticleView.as_view(), name='detail_article'),
    path('create-article/', CreateArticleView.as_view(), name='create_article'),
]
