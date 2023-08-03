from django.urls import path

from catalog.views import home, contacts, ProductView, create
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>', ProductView.as_view(), name='product-detail'),
    path('create', create, name='create'),
]
