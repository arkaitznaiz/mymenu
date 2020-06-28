from django.views.generic.base import TemplateView
from django.shortcuts import render
from products.models import Products
from nutritionalinfo.models import NutritionalInfo

class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['nutritionalinfolistexists'] = True if len(NutritionalInfo.objects.all()) > 0 else False
        context['productlistexists'] = True if len(Products.objects.all()) > 0 else False
        return context

def handler404(request, exception=None):
    return render(request, '404.html', status=404)


def handler500(request, exception=None):
    return render(request, '500.html', status=500)