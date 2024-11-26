from rest_framework import generics
from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework.permissions import IsAuthenticated

class ListaCrearClientesView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]

class DetalleClienteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]
