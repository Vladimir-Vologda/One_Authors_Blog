from django.contrib import admin
from django.contrib.auth.models import Group

from articles.models import ArticleModel


def get_title(self):
    #   Функция, которая обрезает поле
    #   до определённого количества символов
    return self.title[:25]


get_title.short_title = 'Title'


@admin.register(ArticleModel)
class ArticleAdminPanel(admin.ModelAdmin):
    list_display = (
        'id', get_title, 'creation_date', 'update_date', 'is_published',
    )
    list_display_links = (
        get_title,
    )
    list_filter = (
        'is_published',
    )


admin.site.unregister(Group)
