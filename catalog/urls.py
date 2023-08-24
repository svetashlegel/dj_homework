from django.urls import path

from catalog.views import (ProductListView, contacts, ProductDetailView, ProductCreateView, ProductUpdateView,
                           ProductDeleteView)
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('view/<int:pk>', ProductDetailView.as_view(), name='view'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('edit/<int:pk>', ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),
]
