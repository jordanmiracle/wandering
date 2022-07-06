from django import forms
from django.forms import ModelForm, Textarea, TextInput, EmailInput


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name', required=False)
    email = forms.CharField(max_length=200, label='Email', required=False)
    subject = forms.CharField(max_length=100, label='Subject')
    message = forms.CharField(widget=forms.Textarea, label='Message')

    def save(self):
        pass


