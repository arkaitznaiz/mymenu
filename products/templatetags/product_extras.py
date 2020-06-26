from django import template
from django.template.defaultfilters import stringfilter
from products.models import NutritionalValues
from django.shortcuts import get_list_or_404

register = template.Library()

@register.filter
@stringfilter
def detail(value):
    return "<i class='fas fa-eye'></i> %s" % value

@register.filter
def get_nutrivalues(value):
    try:
        list = get_list_or_404(NutritionalValues, product = value.id)
    except:
        list = None
    return list