from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.models import Product
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'category', 'price', 'creation_date', 'last_change_date')
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'category', 'price', 'creation_date', 'last_change_date')
    success_url = reverse_lazy('catalog:home')


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'catalog/contacts.html')


def create(request):
    product_for_create = []
    if request.method == 'POST':
        product = {
            'name': request.POST.get('name'),
            'description': request.POST.get('description'),
            'category': request.POST.get('category'),
            'price': request.POST.get('price'),
            'creation_date': request.POST.get('creation_date'),
            'last_change_date': request.POST.get('last_change_date')
        }
        product_for_create.append(
            Product(**product)
        )
        Product.objects.bulk_create(product_for_create)

    return render(request, 'catalog/create.html')
