from django.shortcuts import render
from catalog.models import Product
from django.views.generic import DetailView


class ProductView(DetailView):
    model = Product
    template_name = 'catalog/product_view.html'
    context_object_name = 'product'


def home(request):

    product_list = Product.objects.all()
    content = {
        'object_list': product_list
    }
    return render(request, 'catalog/home.html', content)


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
