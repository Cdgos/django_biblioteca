from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout
from apps.usuario.forms import FormularioLogin

''' FormView --> Vista basada en clase para trabajar directamente con Forms.
'''


class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')
    #Seguridad
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs): # Sobreescribimos método dispatch de Views (Reconoce la peticion).
        # user viaja por la request asi no se haya iniciado.
        if request.user.is_authenticated:
            # Mandelo al index cuando inicie sesion
            return HttpResponseRedirect(self.get_success_url())
        else:
            #Mandelo al login
            return super(Login, self).dispatch(request, *args, **kwargs)

    # Validar formulario e inicie sesion, se ejecuta por defecto asi no lo redefinamos.
    def form_valid(self, form):
        #login recibe la peticion y una instancia de user para iniciar sesion
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


#LOGOUT, es una funcion que recibe la peticion
def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login')