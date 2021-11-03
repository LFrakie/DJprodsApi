from django.shortcuts import render

from rest_framework import viewsets
from .serializers import ProductoSerializer
from .models import Producto

class ProductoViewSet (viewsets.ModelViewSet):
	queryset=Producto.objects.all()
	serializer_class = ProductoSerializer
# Create your views here.
