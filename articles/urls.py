from django.urls import path

from articles.views import ListArticleView


urlpatterns = [
    path('', ListArticleView.as_view(), name='list_article'),
]
