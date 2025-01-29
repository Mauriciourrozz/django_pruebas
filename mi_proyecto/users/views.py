from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomLoginForm

def custom_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request=request, data=request.POST)
        if form.is_valid():
            # Si el formulario es válido, autenticamos al usuario y lo registramos
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Aquí rediriges a la página principal
    else:
        form = CustomLoginForm()
    
    return render(request, 'users/login.html', {'form': form})

def home(request):
    return render(request, 'users/home.html')
