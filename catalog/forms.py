from django import forms
from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    forbidden_products = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                          'радар']

    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'price', 'creation_date', 'last_change_date')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for product in self.forbidden_products:
            if product in cleaned_data:
                raise forms.ValidationError('Загрузка запрещенных продуктов запрещена.')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        for product in self.forbidden_products:
            if product in cleaned_data:
                raise forms.ValidationError('Загрузка запрещенных продуктов запрещена.')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

