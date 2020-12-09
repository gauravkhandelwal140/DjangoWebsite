from django import forms


class registration(forms.Form):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    phone = forms.CharField(label='Phone No')
    email = forms.EmailField(label='Email id')
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
