from django.urls import path
from .views import ListaCrearClientesView, DetalleClienteView

urlpatterns = [
    path('', ListaCrearClientesView.as_view(), name='clientes'),
    path('<int:pk>/', DetalleClienteView.as_view(), name='detalle_cliente'),
]
