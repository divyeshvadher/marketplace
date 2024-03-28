from django import forms
from .models import *

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("Category", "name", "desc", "price", "image")

        widgets = {
            "Category": forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            "name": forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            "desc": forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            "price": forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            "image": forms.ClearableFileInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
        

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("name", "desc", "price", "image", "is_sold")

        widgets = {
            "name": forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            "desc": forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            "price": forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            "image": forms.ClearableFileInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
        
       