from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

'''AbstractBaseUser es una clase de Django que se utiliza para crear una clase de usuario personalizada para una aplicación. 
Esta clase es una versión simplificada de django.contrib.auth.models.AbstractUser, que es utilizada por el sistema de autenticación de Django para proporcionar 
una clase de usuario básica.'''
class UsuarioManager(BaseUserManager):
    # Las dos cosas que se definen en un Manager es: Crear usuario y Crear administrador
    def create_user(self, email, username, nombres, apellidos, password= None):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico!')

        usuario = self.model(
            username=username,
            email=self.normalize_email(email),
            nombres=nombres,
            apellidos=apellidos
        )
        # Encriptacion set_password() de AbstractBaseUser
        usuario.set_password(password)
        usuario.save()  # Registre en la BD
        return usuario

    def create_superuser(self, username, email, nombres, apellidos, password):
        usuario = self.create_user(
            email,
            username=username,
            nombres=nombres,
            apellidos=apellidos,
            password=password
        )

        usuario.usuario_administrador = True  # Cambiamos su atributo
        usuario.save()
        return usuario

class Usuario(AbstractBaseUser):
    #Sobreescritura de los Usuarios de Django. Podemos añadirle los campos que queramos.
    username = models.CharField('Nombre de usuario', unique=True, max_length=100)
    email = models.EmailField('Correo Electrónico', max_length=254, unique=True)
    nombres = models.CharField('Nombres', max_length=200, blank=True, null=True)
    apellidos = models.CharField('Apellidos', max_length=200, blank=True, null=True)
    imagen = models.ImageField('Imagen de Perfil', upload_to='perfil/', max_length=200, blank=True, null=True)
    usuario_activo = models.BooleanField(default=True)    #Usuario activado puede iniciar sesion
    usuario_administrador = models.BooleanField(default=False)  #Permisos de administrador
    objects = UsuarioManager()

    # Parametro de AbstractBaseUser que hace referencia a cuál es el parámetro único que siempre será requerido
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombres', 'apellidos'] # Datos requeridos al crear el superuser por consola

    def __str__(self):
        return f'{self.nombres},{self.apellidos}'

    # has_perm() y has_module_perms -> Tiene que definirse ya que AbstractBaseUser necesita utilidades para poder usar el admin de Django.
    def has_perm(self, pemr, obj = None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):     # Retorna si un Usuario es administrador o no.
        return self.usuario_administrador