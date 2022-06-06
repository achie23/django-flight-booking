from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    
    name = forms.CharField(max_length=100, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*Full name',
            'class': 'form-control'
            }))
    email = forms.EmailField(max_length=254, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*Email',
            'class': 'form-control'
            }))
    message = forms.CharField(max_length=1000, required=True,
        widget=forms.Textarea(attrs={
            'placeholder': '*Write Message',
            'class': 'form-control',
            'rows': 10,
            }))
    
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message',)