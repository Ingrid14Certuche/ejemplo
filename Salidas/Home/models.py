from django.db import models

# MODELO DE BASE DE DATOS 

#categoria

class Categoria (models.Model):
	nombre				= models.CharField(max_length = 100)
	descripcion 		= models.CharField(max_length = 500)
	
	def __str__ (self):
		return self.nombre

#marca

class Marca (models.Model):
	nombre  			= models.CharField(max_length = 100)

	def __str__ (self):
		return self.nombre

#producto

class Producto(models.Model):
	nombre		          =models.CharField(max_length           = 100)
	descripcion           =models.TextField(max_length           = 500)
	status		          =models.BooleanField(default           = True)
	precio		          =models.DecimalField(max_digits        = 6, decimal_places = 2)
	stock		          =models.IntegerField()

	
	categoria             =models.ManyToManyField(Categoria,null = True, blank   = True)
	Marca                 =models.ForeignKey(Marca, on_delete    = models.CASCADE)


	def __str__ (self):
		return self.nombre


	
		
