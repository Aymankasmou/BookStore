from django import forms   #s19
from .models import book, Category   #s19


class CategoryForm(forms.ModelForm):   #s21
    class Meta:   #s21
        model = Category   #s21
        fields = ['name']   #s21
        widgats = {   #s21
            'name' : forms.TextInput(attrs={'class':'form-control'})   #s21
        }

class BookForm(forms.ModelForm):   #s19
    class Meta:   #s19
        model = book   #s19
        fields = [
            'title',   #s19
            'author',   #s19 
            'photo_book',   #s19
            'photo_author',   #s19
            'pages',   #s19
            'price',    #s19
            'retal_price_day',   #s19
            'retal_period',   #s19
            'total_rental',   #s26
            'status',   #s19
            'Category',   #s19
        ]   #s19
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),    #s19
            'author' : forms.TextInput(attrs={'class': 'form-control'}),    #s19
            'photo_book' : forms.FileInput(attrs={'class': 'form-control'}),    #s19
            'photo_author' : forms.FileInput(attrs={'class': 'form-control'}),    #s19
            'pages' : forms.NumberInput(attrs={'class': 'form-control'}),    #s19
            'price' : forms.NumberInput(attrs={'class': 'form-control'}),    #s19
            'retal_price_day' : forms.NumberInput(attrs={'class': 'form-control' , 'id': 'rentalprice'}),    #s19  s26 'id': 'rentalprice'
            'retal_period' : forms.NumberInput(attrs={'class': 'form-control' , 'id': 'rentaldays'}),    #s19  s26 'id': 'rentaldays'
            'total_rental' : forms.NumberInput(attrs={'class': 'form-control' , 'id': 'totalrental'}),    #s26
            'status' : forms.Select(attrs={'class': 'form-control'}),    #s19
            'Category' : forms.Select(attrs={'class': 'form-control'}),    #s19
        }