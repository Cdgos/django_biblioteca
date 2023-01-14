''' # ========= VISTAS BASADAS EN FUNCIONES ========= # '''
# CREAR AUTOR MEDIANTE FORMS.PY
def crearautor(request):
    if request.method == "POST":
        print(request.POST)
        autor_form = AutorForm(request.POST)  # Reciba los datos que mandaron
        if autor_form.is_valid():  # Funcion de forms
            nom = autor_form.cleaned_data['nombre']  # Los datos estan almacenados aqui
            autor_form.save()  # Metodo modelo, guardar en BD lo que envio el formulario.
            return redirect('index')  # Cuando guarde, redireccione

    else:
        autor_form = AutorForm()  # Pinta el form
        print(autor_form)
    return render(request, 'libro/autor/crear_autor.html', {'autor_form': autor_form})  # Pinta html crearautor, diccionario


# CREAR SIN EL AUTORFORM, MANUALMENTE EN EL TEMPLATE
'''
def crearAutor(request):
    if request.method == "POST":
        print(request.POST) #Recibe los parametros (los input, el form)
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        nacionalidad = request.POST.get('nacionalidad')
        descripcion = request.POST.get('descripcion')

        print(nombre,apellido,nacionalidad,descripcion)

        #Crear una instancia del modelo y pasar parametros
        libro = Autor(nombre = nombre, apellido= apellido, nacionalidad = nacionalidad, descripcion = descripcion)
        libro.save() #Guarde
        return redirect('index')

    return render(request, 'libro/crear_autor.html')
'''


# Consulta a la BD, trae todos los autores y los envia al template renderizados.
def listarAutor(request):
    # ORM Django -> objects es un atributo que tiene todo modelo que interactua con la BD mediante objectmanager, convierte sintaxis django a sql.
    autores = Autor.objects.filter(estado=True);
    return render(request, 'libro/autor/listar_autor.html', {'autores': autores})


''' objects querys methods:
    .create() --> Crear
    .all() --> Trae todos
    .get() --> Devuelve 1 solo
    .filter() --> Devuelve una lista de los que encuentra
'''


# Request y id de la ruta(pk modelo libro)
def editarAutor(request, id):
    # Puede que ese id no exista, se debe manejar el error en un trycatch
    autor_form = None  # Si sucede un error y no entra al try, evitamos error que pinte algo. Por eso un valor none " referenced before assignment"
    error = None  # Lo mismo de arriba
    try:
        # Consulta:
        autor = Autor.objects.get(id=id)  # el id sea igual al id recibido
        # 2 casos posibles: GET(Trae y renderiza info para poder editarla) | POST(Editar y grabar)
        if request.method == "GET":
            # Pedimos la info del formu para renderizarla, pero en este caso solo con la instancia libro.
            autor_form = AutorForm(instance=autor)
        else:
            # Grabamos lo que editamos
            autor_form = AutorForm(request.POST, instance=autor)

            if autor_form.is_valid():
                autor_form.save()
            return redirect('libro:listar_autor')

    except ObjectDoesNotExist as e:
        error = e

    # Reutilice la vista de crear pero esta vez la pinta el form y de paso trae los datos del libro.
    return render(request, 'libro/autor/crear_autor.html', {'autor_form': autor_form, 'error': error})


''' Eliminar: 2 formas
    - Directa --> Borra completamente el registro de la BD.
    - Logica --> Ocultarlo de la vista del cliente
'''

# === ELIMINACIONES DIRECTAS === #
# Forma 1: sin metodo post
'''
def eliminarAutor(request, id):

    #Consulte y obtenga el libro por id
    libro = Autor.objects.get(id = id)

    libro.delete() #Elimine
    return redirect('libro:listar_autor') #Redirige a la misma
'''

# Forma 2: post
'''
def eliminarAutor(request, id):

    #Consulte y obtenga el libro por id
    libro = Autor.objects.get(id = id)

    if request.method == "POST":
        libro.delete() #Elimine
        return redirect('libro:listar_autor') #Redirige a la misma

    return render(request, 'libro/eliminar_autor.html', {'libro':libro})
'''


# === ELIMINACIONES LOGICAS === #
# Cambiar el estado de una instancia en concreto (Deberia existir un campo en el modelo)
def eliminarAutor(request, id):
    # Consulte y obtenga el libro por id
    autor = Autor.objects.get(id=id)

    if request.method == "POST":
        autor.estado = False  # Al cambiar el estado, no se listara, (no elimina).
        autor.save()  # Guarde la edicion
        return redirect('libro:listar_autor')  # Redirige a la misma

    return render(request, 'libro/autor/eliminar_autor.html', {'libro': autor})