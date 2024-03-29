from django import forms

from models import CarBrand, CarModel, CarPrice, User


class CarBrandForm(forms.ModelForm):
    class Meta:
        model = CarBrand
        fields = ['name']

class CarModelForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = ['brand', 'name']

class CarPriceForm(forms.ModelForm):
    class Meta:
        model = CarPrice
        fields = ['car', 'currency', 'price']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
