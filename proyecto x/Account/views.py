from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import RegisterForm, EmailOrUsernameLoginForm

User = get_user_model()


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hashear contraseña
            user.save()
            messages.success(request, "Registro exitoso. Inicia sesión.")
            return redirect('login')
        else:
            messages.error(request, "Corrige los errores del formulario.")
    else:
        form = RegisterForm()

    return render(request, 'core/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = EmailOrUsernameLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Bienvenido, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "Credenciales incorrectas.")
    else:
        form = EmailOrUsernameLoginForm()

    return render(request, 'core/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Sesión cerrada exitosamente.")
    return redirect('login')
