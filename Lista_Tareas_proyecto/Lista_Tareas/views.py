from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from tareas.forms import LoginFormulario, RegistroFormulario  # Asegúrate de tener los nombres correctos


def home_view(request):
    return render(request, "general/home.html")

# Vista para el registro de usuarios
def registro_view(request):
    if request.method == 'POST':
        form = RegistroFormulario(request.POST)
        if form.is_valid():
            user = form.save()  # Guarda el nuevo usuario
            login(request, user)  # Inicia sesión automáticamente
            return redirect('home')  # Redirige a la página de inicio
    else:
        form = RegistroFormulario()
    return render(request, 'general/registro.html', {'form': form})

# Vista para el inicio de sesión
def login_view(request):
    if request.method == 'POST':
        form = LoginFormulario(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('lista_tareas')  # Redirige a la página de inicio
    else:
        form = LoginFormulario()
    return render(request, 'general/login.html', {'form': form})

# Vista para cerrar sesión
def logout_view(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('home')  # Redirige a la página de inicio