from django import forms
from .models import Follow, Messages
from django.core.exceptions import ValidationError


class FollowForm(forms.Form):
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'Your email address', 'class': 'ffin col-12'}))

    def clean_email(self):
        new_email = self.cleaned_data['email'].lower()
        if new_email=='cont':
            raise ValidationError
        if Follow.objects.filter(email__iexact=new_email).count():
            raise ValidationError('Email "{}" is already in use'.format(new_email) )
        return new_email

    def save(self):
        safe_email = Follow.objects.create(
            email=self.cleaned_data['email']
        )
        return safe_email


class MessageForm(forms.Form):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-inp-half col-5'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-inp-half col-5'}))
    email = forms.EmailField(max_length=30, widget=forms.EmailInput(attrs={'class': 'form-inp'}))
    subject = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-inp'}))
    message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'class': 'form-inp-text', 'rows':'4'}))

    def save(self):
        new_mess = Messages.objects.create(
            first_name = self.cleaned_data['first_name'],
            last_name = self.cleaned_data['last_name'],
            email = self.cleaned_data['email'],
            subject = self.cleaned_data['subject'],
            message = self.cleaned_data['message'],
        )
        return new_mess