from django.views.generic.base import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):

    template_name = "index.html"

def handler404(request, exception=None):
    return render(request, '404.html', status=404)


def handler500(request, exception=None):
    return render(request, '500.html', status=500)