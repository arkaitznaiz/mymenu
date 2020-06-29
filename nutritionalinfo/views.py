from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse_lazy

from .models import NutritionalInfo

class NutritionalInfoListView(ListView):
    '''This class based view is intended for listing nutritional info elements from NutritionalInfo model'''

    model = NutritionalInfo
    template_name = 'nutritionalinfo_list.html'
    context_object_name = 'nutrinfos'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(NutritionalInfoListView, self).get_context_data(**kwargs)
        nutrinfos = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(nutrinfos, self.paginate_by)
        try:
            nutrinfos = paginator.page(page)
        except PageNotAnInteger:
            nutrinfos = paginator.page(1)
        except EmptyPage:
            nutrinfos = paginator.page(paginator.num_pages)
        context['nutrinfos'] = nutrinfos
        return context

@method_decorator(login_required, name='dispatch')
class NutritionalInfoCreateView(CreateView):
    '''This class based view is intended for creating a new entry for NutritionalInfo model'''

    model = NutritionalInfo
    template_name = 'nutritionalinfo_create.html'
    fields = ('name', 'unit',)
    success_url = reverse_lazy('nutritionalinfo:nutrinfo-list')
    success_message = "Nutritional information item created!"

class NutritionalInfoDetailView(DetailView):

    model = NutritionalInfo
    template_name = 'nutritionalinfo_detail.html'
    context_object_name = 'nutrinfo'

@method_decorator(login_required, name='dispatch')
class NutritionalInfoUpdateView(UpdateView):

    model = NutritionalInfo
    template_name = 'nutritionalinfo_update.html'
    context_object_name = 'nutrinfo'
    fields = ('name', 'unit',)
    success_message = "Nutritional information item updated!"

    def get_success_url(self):
        return reverse_lazy('nutritionalinfo:nutrinfo-detail', kwargs={'pk': self.object.id})

@method_decorator(login_required, name='dispatch')
class NutritionalInfoDeleteView(DeleteView):
    model = NutritionalInfo
    template_name = 'nutritionalinfo_delete.html'
    success_url = reverse_lazy('nutritionalinfo:nutrinfo-list')
    success_message = "Nutritional information item deleted!"