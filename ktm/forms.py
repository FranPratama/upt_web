from django.forms import ModelForm
from ktm.models import *
from django import forms

class FormKTM(ModelForm):
    class Meta:
        model = ktm
        fields = '__all__'
        exclude = ('no_foto',)

        widgets = {
            'nim' : forms.NumberInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'jurusan' : forms.Select({'class':'form-control'}),
            'tempat_lahir' : forms.TextInput({'class':'form-control'}),
            'tgl_lahir' : forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class':'form-control',
                    'placeholder':'Tahun-bulan-hari',
                    'type':'date'
                    }
            ),
            'alamat' : forms.Textarea({'class':'form-control'}),
            'kec' : forms.TextInput({'class':'form-control'}),
            'kota' : forms.TextInput({'class':'form-control'}),
            'status' : forms.Select({'class':'form-control'}),
            'no_telp' : forms.NumberInput({'class':'form-control'}),
            'foto' : forms.ClearableFileInput(),
        }

        labels = {
            'nim' : 'NIM',
            'tgl_lahir' : 'Tanggal lahir',
            'kec' : 'Kecamatan',
            'no_telp' : 'No. Telepon',
            'foto' : 'Upload Foto',
        }