from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

User = get_user_model()


def article_img(instance, filename):
    #   Функция сохранения изображения в отдельную папку для каждой статьи
    return f'article/{instance.title[:10]}/{filename}'


class ArticleModel(models.Model):
    author = models.ForeignKey(User, verbose_name=_('Author'), on_delete=models.CASCADE, default='1')
    title = models.CharField(_('Article title'), max_length=70, unique=True)
    text = models.TextField(_('Article'))
    image = models.ImageField(_('Article image'), upload_to=article_img, default='default/article_default.jpg')
    creation_date = models.DateTimeField(_('Date of creation'), auto_now_add=True)
    update_date = models.DateTimeField(_('Update date'), auto_now=True)
    is_published = models.BooleanField(_('Is published'), default=False)
    slug = models.SlugField(_('URL address'), unique=True, db_index=True)

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
        ordering = (
            '-update_date',
        )

    def __str__(self):
        return f'{self.title}'

    def translate_title(self):
        #   Функция, которая заменяет буквы(знаки, символы),
        #   в данном случае заменяет кириллицу на латиницу.
        title = self.title.translate(
            str.maketrans(
                "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
                "abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA"
            )
        )
        return title

    def save(self, *args, **kwargs):
        #   Функция создания Slug, если он отсутствует
        if not self.slug:
            #   Slugify, создаёт удобочитаемый URL-address, по заданному полю
            self.slug = slugify(self.translate_title())
        return super(ArticleModel, self).save(**kwargs)

    def get_absolute_url(self):
        return reverse('detail_article', kwargs={'slug': self.slug})
