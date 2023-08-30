from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import (ProductListView, contacts, ProductDetailView, ProductCreateView, ProductUpdateView,
                           ProductDeleteView, product_edit_denial, categories)
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('view/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='view'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('edit/<int:pk>', ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),
    path('denial/<str:task>', product_edit_denial, name='denial'),
    path('categories/', categories, name='categories'),
]
