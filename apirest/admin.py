from django.contrib import admin
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
										# Precio
	list_display = ('nombres', 'marca', 'precio', 'codigo','emailemp', 'id')

admin.site.register(Producto, ProductoAdmin)

# Register your models here.
