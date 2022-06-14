from django import forms
from django.forms import ModelForm
from django_countries.fields import CountryField
from .models import Contact



class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_no', 'country']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'phone_no': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'country': forms.TextInput(attrs={'placeholder': 'Country'}),
            'message': forms.TextInput(attrs={'placeholder': 'Message...'}),


        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

# class ContactForm(forms.Form):
#     name = forms.CharField(label='Name', max_length=100)
#     email = forms.EmailField(label='Email')
#     phone_no = forms.CharField(label='Phone Number', max_length=12)
#     country = forms.CharField(label='Enter Your Country')
#     message = forms.CharField(label='Message here')
#
#     def __init__(self, *args, **kwargs):
#         super(ContactForm, self).__init__(*args, **kwargs)
#
#         for name, field in self.fields.items():
#             field.widget.attrs.update({'class': 'input', ''})

