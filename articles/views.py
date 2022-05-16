from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    ListView, DetailView, CreateView
)

from articles.forms import ArticleForm
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


class DetailArticleView(DetailView):
    model = ArticleModel
    template_name = 'article/detail_article.html'
    context_object_name = 'detail_article'

    def get_context_data(self, **kwargs):
        context = super(DetailArticleView, self).get_context_data(**kwargs)
        context['title'] = context['detail_article']
        return context


class CreateArticleView(CreateView):
    form_class = ArticleForm
    model = ArticleModel
    template_name = 'article/create_article.html'
    context_object_name = 'create_article'
    # success_url = reverse_lazy('list_article')
    # # SUCCESS_URL - Можно присвоить переход на любую страницу,
    # # либо не прописывать, и тогда, благодаря методу get_absolute_url (из models.py),
    # # пользователь будет перенаправлен на страницу статьи

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        #   Функция, которая позволяет публиковать статьи только персоналу (is_staff=True)
        if not user.is_staff:
            raise Http404('Publications can only be made by employees!')
        return super(CreateArticleView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        #   Функция, автоматически присваивающая полю author, текущего пользователя
        form.instance.author = self.request.user
        return super(CreateArticleView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateArticleView, self).get_context_data(**kwargs)
        context['title'] = _('Create article')
        return context
