from django.template import Library, Variable
from django.conf import settings
from django import template
from tags.baseconv import base62
import random

register = Library()

@register.simple_tag
def root_url():
    return settings.ROOT_URL

@register.simple_tag
def media_url():
    return settings.MEDIA_URL


@register.filter
def shorturl(value):
    return base62.from_decimal(value)
