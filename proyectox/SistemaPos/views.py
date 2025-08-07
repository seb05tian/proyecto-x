# habits/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home_view(request):
    return render(request, "core/home.html")


def Mesero1(request):
    return render(request, "core/MeseroInicial.html")
