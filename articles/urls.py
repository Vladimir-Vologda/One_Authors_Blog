from django.urls import path

from articles.views import (
    ListArticleView, DetailArticleView
)

urlpatterns = [
    path('', ListArticleView.as_view(), name='list_article'),
    path('<slug:slug>/', DetailArticleView.as_view(), name='detail_article'),
]
