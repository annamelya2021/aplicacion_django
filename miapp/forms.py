from django import forms
from .models import Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
        }
        help_texts = {
            'nombre': 'Ingrese su nombre',
            'apellido': 'Ingrese su apellido',
        }
        error_messages = {
            'nombre': {
                'required': 'El nombre es obligatorio',
            },
            'apellido': {
                'required': 'El apellido es obligatorio',
            },
        }   
    
    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        apellido = cleaned_data.get('apellido')
        
        if nombre and len(nombre) < 3:
            self.add_error('nombre', 'Debe tener al menos 3 caracteres')
        
        if apellido and len(apellido) < 3:
            self.add_error('apellido', 'Debe tener al menos 3 caracteres')
        
        if nombre and apellido and nombre == apellido:
            self.add_error(None, 'Nombre y apellido no pueden ser iguales')
        
        return cleaned_data
    
