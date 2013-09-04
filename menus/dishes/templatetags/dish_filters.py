from django import template
from django.template.defaultfilters import stringfilter
import re

register= template.Library()

@register.filter(name='title', is_safe=True)
@stringfilter
def title(string):
    return string.title()

@register.filter(name='format_price', is_safe=True)
@stringfilter
def format_price(string):
    try:
        return "${price:4,}".format(price=float(string))
    except ValueError:
        return string
