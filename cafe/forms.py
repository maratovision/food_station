from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['food'].widget.attrs.update({'class': 'row' , 'type': 'text'})
        self.fields['quantity'].widget.attrs.update({'class': 'row' , 'type': 'text'})
        self.fields['name'].widget.attrs.update({'class': 'row' , 'type': 'text'})
        self.fields['phone'].widget.attrs.update({'class': 'row' , 'type': 'text'})
        self.fields['email'].widget.attrs.update({'class': 'row' , 'type': 'text'})
        self.fields['city'].widget.attrs.update({'class': 'row' , 'type': 'text'})
        self.fields['address'].widget.attrs.update({'class': 'row' , 'type': 'text'})
        self.fields['house'].widget.attrs.update({'class': 'row' , 'type': 'text'})
        self.fields['user'].widget.attrs.update({'class': 'row' , 'type': 'text'})
        self.fields['pay_method'].widget.attrs.update({'class': 'row' , 'type': 'text'})



class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control form-control-lg', 'type': 'text', 'name':'name', 'placeholder': 'Enter your username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control form-control-lg', 'type': 'email', 'name':'email', 'placeholder': 'Enter your email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control form-control-lg', 'type': 'password', 'name':'password', 'placeholder': 'Enter your password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control form-control-lg', 'type': 'password', 'name':'password', 'placeholder': 'Confirm your password'})


class TestimonialsForm(forms.ModelForm):

    class Meta:
        model = Testimonials
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'col-md-6 col-sm-12', 'name': 'name', 'type': 'text', 'id': 'name', 'placeholder': 'Your name:'})
        self.fields['subject'].widget.attrs.update({'class': 'col-md-12 col-sm-12' , 'name': 'subject', 'type': 'text', 'id': 'subject', 'placeholder': 'Subject:'})
        self.fields['massage'].widget.attrs.update({'class': 'col-md-12 col-sm-12' , 'name': 'massage', 'rows': '6', 'id': 'massage', 'placeholder': 'Massage:'})


class RateForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = '__all__'