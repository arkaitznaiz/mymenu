from django import template
from django.template.defaultfilters import stringfilter
from django.shortcuts import get_list_or_404

register = template.Library()

@register.filter
@stringfilter
def detail(value):
    return "<i class='fas fa-eye'></i> %s" % value
