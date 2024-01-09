from django.forms import ModelForm
from hotspot.models import *
from django import forms

class FormHotspot(ModelForm):
    class Meta:
        model = hotspot
        fields = '__all__'

        widgets = {
            'email' : forms.EmailInput({'class':'form-control'}),
            'no_telp' : forms.NumberInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'username' : forms.NumberInput({'class':'form-control'}),
            'password' : forms.PasswordInput({'class':'form-control'}),
        }

        labels = {
            'no_telp' : 'No. Telepon',
            'username' : 'Username (Isi sesuai dengan NIM)',
            'password' : 'Password (Maksimal 15 karakter)'
        }