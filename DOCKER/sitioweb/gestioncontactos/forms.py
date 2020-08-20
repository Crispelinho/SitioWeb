from django import forms
from .models import Contacto


class ContactosForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = [
        'nombre',
        'apellido',
        'Ncelular',
        'fotografia',
        'correo'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido' : forms.TextInput(attrs={'class':'form-control'}),
            'Ncelular' : forms.TextInput(attrs={'class':'form-control', 'type':'number'}),
            'fotografia' : forms.TextInput(attrs={'class':'form-control','type':'file'}),
            'correo' : forms.TextInput(attrs={'class':'form-control', 'type':'email'})   
        }
