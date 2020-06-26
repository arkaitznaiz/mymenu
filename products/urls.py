from django.urls import path
from django.conf.urls import url
from django_filters.views import FilterView
from .models import Products

from . import views

app_name = 'products'

urlpatterns = [
    path('create/', views.ProductsCreateView.as_view(), name='product-create'),
    path('<int:pk>/', views.ProductsDetailView.as_view(), name='product-detail'),
    path('<int:pk>/update/', views.ProductsUpdateView.as_view(), name='product-update'),
    path('<int:pk>/delete/', views.ProductsDeleteView.as_view(), name='product-delete'),
    path('<int:pk>/nutrinfo/create/', views.NutritionalValuesCreateView.as_view(), name='nutritionalvalues-create'),
    path('nutrinfo/<int:pk>/', views.NutritionalValuesDetailView.as_view(), name='nutritionalvalues-detail'),
    path('nutrinfo/<int:pk>/update/', views.NutritionalValuesUpdateView.as_view(), name='nutritionalvalues-update'),
    path('nutrinfo/<int:pk>/delete/', views.NutritionalValuesDeleteView.as_view(), name='nutritionalvalues-delete'),
    url(r'^$', FilterView.as_view(model=Products, filterset_fields=['name', 'active']), name='product-list'),
]