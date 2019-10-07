# -*- coding: utf-8 -*-
# Create your models here.

from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': u'Имя'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': u'Емейл', 'class': 'input-field'}))
    phone = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': u'Телефон'}))
