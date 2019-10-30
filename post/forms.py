# -*- coding: utf-8 -*-
# Create your models here.

from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': u'Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': u'Email', 'class': 'input-field'}))
    phone = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': u'Phone'}))


class SearchForm(forms.Form):
    q = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'input-field'}))
