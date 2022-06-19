from django import forms
from django.forms import ModelForm, Textarea, TextInput, EmailInput


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=200)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)

    def save(self):
        pass


