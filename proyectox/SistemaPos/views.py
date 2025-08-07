# habits/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Sala, Mesa, Pedido, Producto, Categoria, DetallePedido
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@login_required
def home_view(request):
    return render(request, "core/home.html")


def Mesero1(request):
    return render(request, "core/MeseroInicial.html")


def vista_sala(request, sala_id):
    sala = get_object_or_404(Sala, id=sala_id)
    salas = Sala.objects.prefetch_related('mesa_set').all()
    categorias = Categoria.objects.all()
    productos = Producto.objects.select_related('categoria').all()

    context = {
        'sala': sala,
        'salas': salas,
        'categorias': categorias,
        'productos': productos,
    }
    return render(request, "core/MeseroInicial.html", context)


@csrf_exempt

def crear_pedido(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mesa_id = data.get('mesa_id')
        productos = data.get('productos', [])

        mesa = get_object_or_404(Mesa, id=mesa_id)
        pedido = Pedido.objects.create(mesa=mesa, usuario=request.user)

        for p in productos:
            producto = get_object_or_404(Producto, id=p['id'])
            DetallePedido.objects.create(
                pedido=pedido,
                producto=producto,
                cantidad=1,
                precio_unitario=producto.precio,
                subtotal=producto.precio
            )

        mesa.estado = 'ocupada'
        mesa.save()

        return JsonResponse({'status': 'ok'})