from django.contrib.auth.models import User
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django.forms import ModelForm
from bookstore.models import Book
from django import forms


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'year', 'desc')        


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

