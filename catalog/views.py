from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.forms import inlineformset_factory

from catalog.models import Product, Version
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from catalog.forms import ProductForm, VersionForm


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST)
        else:
            context_data['formset'] = VersionFormset()
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            self.object.is_active = False
            raise Http404("Вы не являетесь создателем данного товара, у вас нет прав на его редактирование.")
        return self.object

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        return super().form_valid(form)


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        versions = obj.version_set.all()
        active_versions = []
        for version in versions:
            if version.status:
                active_versions.append(version)
        context["product_version"] = active_versions
        return context


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            self.object.is_active = False
            raise Http404("Вы не являетесь создателем данного товара, у вас нет прав на его удаление.")
        return self.object


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'catalog/contacts.html')


def product_edit_denial(request, task):
    context = {
        'denied_task': task,
    }
    return render(request, 'catalog/edit_denial.html', context)
