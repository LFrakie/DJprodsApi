from django.shortcuts import render

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from apirest.models import Producto

class ProductoListView(ListView):
	model = Producto
	#template_name = ".html"

# Create your views here.
