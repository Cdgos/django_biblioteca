from django import forms

from .models import Autor, Libro


#Esta clase formulario pertenece al modelo libro.
class AutorForm(forms.ModelForm):
    #Definir los metadatos. Django pinta el html por nosotros con estos campos:
    class Meta:
        model = Autor
        fields = ["nombre","apellido","nacionalidad","descripcion"] #Todos los campos que serán rellenados cuando creen un nuevo libro.

        # Pintar etiquetas label en el template
        labels = {
            'nombre': 'Nombre del libro',
            'apellido': 'Apellido del libro',
            'nacionalidad': 'Nacionalidad del libro',
            'descripcion': 'Pequeña descripción',
        }

        # Pintar estilos en el template
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del Autor',
                    'id': 'nombre'
                }
            ),
            'apellido': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el apellido del Autor',
                    'id': 'apellido'
                }
            ),
            'nacionalidad': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese la nacionalidad del Autor',
                    'id': 'nacionalidad'
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese una breve descripción para el Autor',
                    'id': 'descripcion'
                }
            )
        }

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ("titulo", "autor_id", "fecha_publicacion") #Tupla

        labels = {
            'titulo': 'Titulo del Libro',
            'autor_id': 'Autor(es) del Libro',
            'fecha_publicacion': 'Fecha de publicación del Libro'
        }

        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el título del Libro'
                }
            ),
            'autor_id': forms.SelectMultiple(
                attrs= {
                    'class': 'form-control'
                }
            ),
            'fecha_publicacion': forms.SelectDateWidget(
                attrs= {
                    'class': 'form-control'
                }
            )
        }
