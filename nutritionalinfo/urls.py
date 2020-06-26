from django.urls import path

from . import views

app_name = 'nutritionalinfo'

urlpatterns = [
    path('', views.NutritionalInfoListView.as_view(), name='nutrinfo-list'),
    path('create/', views.NutritionalInfoCreateView.as_view(), name='nutrinfo-create'),
    path('<int:pk>/', views.NutritionalInfoDetailView.as_view(), name='nutrinfo-detail'),
    path('<int:pk>/update/', views.NutritionalInfoUpdateView.as_view(), name='nutrinfo-update'),
    path('<int:pk>/delete/', views.NutritionalInfoDeleteView.as_view(), name='nutrinfo-delete'),
]