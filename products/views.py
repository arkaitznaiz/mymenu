from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Products, NutritionalValues


@method_decorator(login_required, name='dispatch')
class ProductsCreateView(CreateView):
    '''This class based view is intended for creating a new entry for Products model'''

    model = Products
    template_name = 'products_create.html'
    fields = ('name', 'description', 'active',)
    success_url = reverse_lazy('products:product-list')
    success_message = "Product item created!"

class ProductsDetailView(DetailView):

    model = Products
    template_name = 'products_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductsDetailView, self).get_context_data(**kwargs)
        try:
            context['nutritionalvalues'] = get_list_or_404(NutritionalValues, product=self.object.pk)
        except:
            context['nutritionalvalues'] = None
        return context

@method_decorator(login_required, name='dispatch')
class ProductsUpdateView(UpdateView):

    model = Products
    template_name = 'products_update.html'
    context_object_name = 'product'
    fields = ('name', 'description', 'active')
    success_message = "Product item updated!"

    def get_success_url(self):
        return reverse_lazy('products:product-detail', kwargs={'pk': self.object.id})

@method_decorator(login_required, name='dispatch')
class ProductsDeleteView(DeleteView):
    model = Products
    template_name = 'products_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('products:product-list')
    success_message = "Product item deleted!"


@method_decorator(login_required, name='dispatch')
class NutritionalValuesCreateView(CreateView):
    '''This class based view is intended for creating a new entry for NutritionalValues model'''

    model = NutritionalValues
    template_name = 'nutritionalvalues_create.html'
    fields = ('nutritionalinfo', 'value',)
    success_message = "Nutritional value item created!"

    def get_context_data(self, **kwargs):
        context = super(NutritionalValuesCreateView, self).get_context_data(**kwargs)
        context['product'] = get_object_or_404(Products, id=self.kwargs.get('pk'))
        return context
    
    def get_success_url(self):
        return reverse_lazy('products:product-detail', kwargs={'pk':self.kwargs.get('pk')})

    def form_valid(self, form):
        form.instance.product = get_object_or_404(Products, id=self.kwargs.get('pk'))
        return super().form_valid(form)

class NutritionalValuesDetailView(DetailView):

    model = NutritionalValues
    template_name = 'nutritionalvalues_detail.html'
    context_object_name = 'nutritionalvalue'

@method_decorator(login_required, name='dispatch')
class NutritionalValuesUpdateView(UpdateView):

    model = NutritionalValues
    template_name = 'nutritionalvalues_update.html'
    context_object_name = 'nutritionalvalue'
    fields = ('value',)
    success_message = "Nutritional value item updated!"

    def get_success_url(self):
        return reverse_lazy('products:product-detail', kwargs={'pk': self.object.product.id })
    
    def get_context_data(self, **kwargs):
        context = super(NutritionalValuesUpdateView, self).get_context_data(**kwargs)
        context['product'] = get_object_or_404(NutritionalValues, id=self.kwargs.get('pk')).product
        return context

@method_decorator(login_required, name='dispatch')
class NutritionalValuesDeleteView(DeleteView):
    model = NutritionalValues
    template_name = 'nutritionalvalues_delete.html'
    context_object_name = 'nutritionalvalue'
    success_message = "Nutritional value item deleted!"
    
    def get_success_url(self):
        return reverse_lazy('products:product-detail', kwargs={'pk': self.object.product.id })

    def get_context_data(self, **kwargs):
        context = super(NutritionalValuesDeleteView, self).get_context_data(**kwargs)
        context['product'] = get_object_or_404(NutritionalValues, id=self.kwargs.get('pk')).product
        return context