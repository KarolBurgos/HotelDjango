from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse

class Habitacion(models.Model):
	"""Habitacion"""
	numero = models.CharField(max_length=50)
	def __str__(self):
		return self.numero

	def get_absolute_url(self):
		return reverse('habitacion-list')

class TipoHabitacion(models.Model):
	"""docstring for ClassName"""

	tipo = models.CharField(max_length=50)
	photo = models.ImageField(upload_to='photos/')
	precio = models.CharField(max_length=50)
	cantidadPersonas = models.CharField(max_length=50)
	idHabitacion = models.ForeignKey('Habitacion',on_delete=models.PROTECT)

	def __str__(self):
		
		return self.tipo

	def get_absolute_url(self):
		return reverse('tipohabitacion-list')

class Cliente(models.Model):
	"""docstring for Cliente"""
	identificacion = models.CharField(max_length=50,primary_key=True)
	nombre = models.CharField(max_length=60)
	apellido = models.CharField(max_length=60)
	telefono = models.CharField(max_length=60)
	email = models.CharField(max_length=100)

	def __str__(self):
		
		return self.identificacion

	def get_absolute_url(self):
		return reverse('cliente-list')
		

class Reserva(models.Model):
	"""docstring for Reserva"""

	fechaIngreso = models.DateField()
	fechaSalida = models.DateField()
	idTipoHabitacion = models.ForeignKey('TipoHabitacion',on_delete=models.PROTECT)
	idCliente = models.ForeignKey('Cliente',on_delete=models.PROTECT)
	idTipoReserva = models.ForeignKey('TipoReserva',on_delete=models.PROTECT)
	
	def __str__(self):
		
		return str(self.idCliente)

	def get_absolute_url(self):
		return reverse('reserva-list')


class Pago(models.Model):
	"""docstring for Pago"""

	total = models.CharField(max_length=60)
	idCliente = models.ForeignKey('Reserva',on_delete=models.PROTECT)

	def __str__(self):
		
		return str(self.total)

	def get_absolute_url(self):
		return reverse('pago-list')

class TipoReserva(models.Model):
	"""docstring for TipoReserva"""
	tipo =models.CharField(max_length=60)

	def __str__(self):
		
		return self.tipo

	def get_absolute_url(self):
		return reverse('tiporeserva-list')

@receiver(post_delete, sender=TipoHabitacion)
def photo_delete(sender, instance, **kwargs):
	""" Borra los ficheros de las fotos que se eliminan."""
	instance.photo.delete(False)
# Create your models here.
