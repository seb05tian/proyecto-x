from django.contrib import admin
from .models import (
    Categoria, Producto, Sala, Mesa,
    Pedido, DetallePedido, MovimientoCaja, Licencia
)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'precio', 'imprime_en_cocina', 'categoria')
    list_filter = ('tipo', 'categoria', 'imprime_en_cocina')
    search_fields = ('nombre',)


@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'sala', 'estado')
    list_filter = ('estado', 'sala')
    search_fields = ('numero',)


class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 0
    readonly_fields = ('precio_unitario', 'subtotal')


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'mesa', 'usuario', 'estado', 'fecha')
    list_filter = ('estado', 'fecha')
    search_fields = ('mesa__numero', 'usuario__username')
    inlines = [DetallePedidoInline]


@admin.register(MovimientoCaja)
class MovimientoCajaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'tipo_movimiento', 'monto', 'usuario')
    list_filter = ('tipo_movimiento', 'fecha')
    search_fields = ('concepto',)


@admin.register(Licencia)
class LicenciaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'estado', 'fecha_activacion', 'fecha_expiracion')
    list_filter = ('estado',)
    search_fields = ('codigo',)
