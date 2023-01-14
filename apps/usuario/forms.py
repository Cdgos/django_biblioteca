# Formulario para el login (Forms por defecto de django para autenticacion)
from django.contrib.auth.forms import AuthenticationForm
class FormularioLogin(AuthenticationForm):

    # Formulario a pintar
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

