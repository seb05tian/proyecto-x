from django.urls import path
from .views import home_view, Mesero1, vista_sala, crear_pedido

urlpatterns = [
    path("home/", home_view, name="home"),
    path("Mesero1/", Mesero1, name="Mesero"),
    path('sala/<int:sala_id>/', vista_sala, name='vista_sala'),
    path('api/crear_pedido/', crear_pedido, name='crear_pedido'),
]
