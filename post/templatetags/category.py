from django import template
from django.shortcuts import get_object_or_404

from post.models import GlavCategoryForKatalog

register = template.Library()


@register.filter(name=u'category_set')
def category_set(slug):
    podglavnyi = get_object_or_404(GlavCategoryForKatalog, slug__icontains=slug, language__name__icontains=u'ru')
    return podglavnyi.categoryforkatalog_set.filter(language__name__icontains=u'ru')


