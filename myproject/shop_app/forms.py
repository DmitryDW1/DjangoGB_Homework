from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 
            'description', 
            'price', 
            'quantity', 
            'photo'
            ]


class AddProduct(forms.Form):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
            'placeholder': 'new product name'}
            )
        )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control', 
                   'placeholder': 'product description'}
            )
        )

    price = forms.FloatField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}
            )
        )
    quantity = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}
            )
        )
    photo = forms.ImageField(
        required=False,widget=forms.ClearableFileInput(
            attrs={'class': 'form-control-file'}
            )
        )