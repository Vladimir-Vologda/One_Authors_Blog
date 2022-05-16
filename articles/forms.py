from django import forms

from articles.models import ArticleModel


class ArticleForm(forms.ModelForm):

    class Meta:
        model = ArticleModel
        fields = (
            'title', 'text', 'image', 'is_published',
        )
