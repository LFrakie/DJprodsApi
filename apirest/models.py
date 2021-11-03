from django.db import models

class Producto(models.Model):
	
	nombres=models.CharField(max_length=50)
	marca=models.CharField(max_length=50)
	codigo=models.CharField(max_length=8)
	emailemp=models.EmailField(max_length=50)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = ("Producto")
		verbose_name_plural = ("Productos")

	def __str__(self):
		return self.nombres

