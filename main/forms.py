from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your name', 'class': 'form-attr'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter Email Address', 'class': 'form-attr'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Message Title', 'class': 'form-attr'}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Message goes here . . .', 'class': 'form-attr'}))

    class Meta:
        model = Contact
        exclude = ('created', 'updated')

    def clean(self):
        super(ContactForm, self).clean()

        first_name = self.cleaned_data.get('first_name')
        email = self.cleaned_data.get('email')
        title = self.cleaned_data.get('title')
        message = self.cleaned_data.get('message')

        return self.cleaned_data
