from django.urls import path
from .views import home_view, Mesero1


urlpatterns = [
    path("home/", home_view, name="home"),
    path("Mesero1/", Mesero1, name="Mesero"),
]
