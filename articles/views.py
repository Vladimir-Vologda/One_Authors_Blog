from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView

from articles.models import ArticleModel


class ListArticleView(ListView):
    model = ArticleModel
    template_name = 'article/list_article.html'
    context_object_name = 'list_article'

    def get_queryset(self):
        #   Функция, благодаря которой, будут передаваться
        #   только опубликованные статьи (is_published=True)
        return ArticleModel.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListArticleView, self).get_context_data(**kwargs)
        context['title'] = _("Article's")
        return context

