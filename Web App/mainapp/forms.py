from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_name', )

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category_name', 'item_name', 'item_description', 'founder_name', 'founder_number')