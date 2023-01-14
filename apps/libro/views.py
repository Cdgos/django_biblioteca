from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .forms import AutorForm, LibroForm
from .models import Autor, Libro

'''VISTAS BASADAS EN CLASES

VIEW --> Clase general de la cual heredan las demas clases. Tiene metodos get(),post(), put()etc.

    TemplateView() --> Vista basada en clase para renderizar un template. Utiliza el método get() es el correcto.
        - templane_name = 'nombreTemplate' (ruta/archivo/etc)

    ListView() --> Vista basada en clase para listar.
        - model = NombreModelo --> Indicarle nombre del modelo
        - queryset = consulta. Por defecto hace un objects.all()
        - context_object_name = '' --> Nombre valores que retorna la view de la consulta queryset. Por defecto se llama object_list.

        - template_name = Lo usamos aqui tambien para renderizar.

    UpdateView() --> Vista basada en clase para editar
        - model
        - template_name
        - form_class = ClaseForm --> Indicarle que usaré un form que he creado
        - success_url = reverse_lazy(url) --> Indicarle que redirija a la url cuando edite.


Cilo de VIEW:
    Esto es el orden/lo primero que hace Django cuando se llama View (Es como un método constructor)

    1.- dispatch(): Valida la petición y elige que metodo HTTP se utilizo para la solicitud.
    2.- http_method_not_allowed(): retorna un error cuando se utiliza un metodo HTTP no soportado o definido (si dispatch no lo identificó)
    3.- options(): Retorna lista de nombres permitidos para la vista, hace uso HTTP
'''

''' 1. Clase inicio como funciona por debajo (Codigo nativo)
class Inicio(TemplateView):
    def get(self, request, *args, **kwargs): #parametros que recibe si o si get.
        return render(request, 'index.html')
'''

# 2. Podemos reducir mucho mas el codigo para renderizar un template:
class Inicio(TemplateView):
    template_name = 'index.html'
    #Despues de esto podemos sobreescribir el metodo get si tenemos otra logica

# ====== AUTORES ====== #
class ListadoAutor(ListView):
    model = Autor
    template_name = 'libro/autor/listar_autor.html'
    context_object_name = 'autores'
    queryset = Autor.objects.filter(estado = True)

class ActualizarAutor(UpdateView):
    model = Autor
    template_name = 'libro/autor/crear_autor.html'
    form_class = AutorForm
    success_url = reverse_lazy('libro:listar_autor') #Redirigir cuando edite


class CrearAutor(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'libro/autor/crear_autor.html'
    success_url = reverse_lazy('libro:listar_autor')


class EliminarAutor(DeleteView):
    model = Autor
    #success_url = reverse_lazy('libro:listar_autor') Si es eliminacion logica no podemos usar success, debe ser redirect

    #Por defecto hace eliminacion directa y usa el confirm_delete.html. Sino queremos, reescribimos post:
    def post(self, request, pk, *args, **kwargs):
        object = Autor.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('libro:listar_autor')

# ====== LIBROS CRUD ====== #
class ListadoLibros(ListView):
    model = Libro
    template_name = 'libro/libro/listar_libro.html'
    queryset = Libro.objects.filter(estado=True)
    # Si la queryset no se indica será por defecto = Libro.objects.all() y se llama object_list

class CrearLibro(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/crear_libro.html'
    success_url = reverse_lazy('libro:listado_libros')

class ActualizarLibro(UpdateView):
    model = Libro
    template_name = 'libro/libro/crear_libro.html'
    form_class = LibroForm
    success_url = reverse_lazy('libro:listado_libros')

class EliminarLibro(DeleteView):
    model = Libro

    def post(self, request, pk, *args, **kwargs):
        object = Libro.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('libro:listado_libros')

''' APUNTES
objects querys methods:
    .create() --> Crear
    .all() --> Trae todos
    .get() --> Devuelve 1 solo
    .filter() --> Devuelve una lista de los que encuentra

Eliminar: 2 formas
    - Directa --> Borra completamente el registro de la BD.
    - Logica --> Ocultarlo de la vista del cliente (Cambiar el estado de una instancia en concreto (Deberia existir un campo en el modelo))
'''