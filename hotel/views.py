from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from .serializers import HabitacionSerializer, ClienteSerializer
from hotel.models import Habitacion,TipoHabitacion,Cliente,Reserva,Pago,TipoReserva

class HabitacionViewSet(viewsets.ModelViewSet):
	queryset = Habitacion.objects.all()
	serializer_class = HabitacionSerializer


class ClienteViewSet(viewsets.ModelViewSet):
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer
	
@login_required
def log(request):
	return render(request, 'hotel/login.html')

def inicio(request):
	return render(request, 'inicio.html')

@login_required
def base(request):
	return render(request, 'base.html')

@login_required
def first_view(request):
	return HttpResponse('Esta es mi primera vista')

@login_required
def habitacion(request):
	habitacion_list = Habitacion.objects.all()
	context = {'object_list': habitacion_list}
	return render(request,'hotel/habitacion.html',context)

@method_decorator(login_required, name='dispatch')
def habitacion_detail(request, habitacion_id):
	habitacion = Habitacion.objects.get(id=habitacion_id)
	context = {'object':habitacion}
	return render(request, 'hotel/habitacion_detail.html',context)

@method_decorator(login_required, name='dispatch')
class HabitacionUpdate(UpdateView):
	"""docstring for HabitacionUpdate"""
	model=Habitacion
	fields = '__all__'

@method_decorator(login_required, name='dispatch')
class HabitacionCreate(CreateView):
	"""docstring for HabitacionCreate"""
	model= Habitacion
	fields = '__all__'

@method_decorator(login_required, name='dispatch')	
class HabitacionDelete(DeleteView):
	"""docstring for HabitacionDelete"""
	model= Habitacion
	success_url = reverse_lazy('habitacion-list')

#Para la clase TipoHabitacion

class TipoHabitacionListView(ListView):
	"""docstring for PhotoListView"""
	model = TipoHabitacion

class TipoHabitacionDetailView(DetailView):
	"""docstring for PhotoDetailView"""
	model= TipoHabitacion

class TipoHabitacionUpdate(UpdateView):
	"""docstring for HabitacionUpdate"""
	model=TipoHabitacion
	fields = '__all__'

class TipoHabitacionCreate(CreateView):
	"""docstring for HabitacionCreate"""
	model= TipoHabitacion
	fields = '__all__'
	
class TipoHabitacionDelete(DeleteView):
	"""docstring for HabitacionDelete"""
	model= TipoHabitacion
	success_url = reverse_lazy('tipohabitacion-list')

#Para la clase Cliente
@method_decorator(login_required, name='dispatch')
class ClienteListView(ListView):
	"""docstring for PhotoListView"""
	model = Cliente

@method_decorator(login_required, name='dispatch')
class ClienteDetailView(DetailView):
	"""docstring for PhotoDetailView"""
	model= Cliente

@method_decorator(login_required, name='dispatch')
class ClienteUpdate(UpdateView):
	"""docstring for HabitacionUpdate"""
	model=Cliente
	fields = '__all__'

@method_decorator(login_required, name='dispatch')
class ClienteCreate(CreateView):
	"""docstring for HabitacionCreate"""
	model= Cliente
	fields = '__all__'

@method_decorator(login_required, name='dispatch')	
class ClienteDelete(DeleteView):
	"""docstring for HabitacionDelete"""
	model= Cliente
	success_url = reverse_lazy('cliente-list')


#Para la clase PAGO
@method_decorator(login_required, name='dispatch')
class PagoListView(ListView):
	"""docstring for PhotoListView"""
	model = Pago

@method_decorator(login_required, name='dispatch')
class PagoDetailView(DetailView):
	"""docstring for PhotoDetailView"""
	model= Pago

@method_decorator(login_required, name='dispatch')
class PagoUpdate(UpdateView):
	"""docstring for HabitacionUpdate"""
	model=Pago
	fields = '__all__'

@method_decorator(login_required, name='dispatch')
class PagoCreate(CreateView):
	"""docstring for HabitacionCreate"""
	model= Pago
	fields = '__all__'
	
@method_decorator(login_required, name='dispatch')
class PagoDelete(DeleteView):
	"""docstring for HabitacionDelete"""
	model= Pago
	success_url = reverse_lazy('pago-list')

#Para la clase RESERVA

@method_decorator(login_required, name='dispatch')
class ReservaListView(ListView):
	"""docstring for ReservaListView"""
	model = Reserva

@method_decorator(login_required, name='dispatch')
class ReservaDetailView(DetailView):
	"""docstring for ReservaDetailView"""
	model= Reserva

@method_decorator(login_required, name='dispatch')
class ReservaUpdate(UpdateView):
	"""docstring for ReservaUpdate"""
	model=Reserva
	fields = '__all__'

@method_decorator(login_required, name='dispatch')
class ReservaCreate(CreateView):
	"""docstring for ReservaCreate"""
	model= Reserva
	fields = '__all__'

@method_decorator(login_required, name='dispatch')	
class ReservaDelete(DeleteView):
	"""docstring for ReservaDelete"""
	model= Reserva
	success_url = reverse_lazy('reserva-list')

#Para la clase TIPO DE RESERVA

class TipoReservaListView(ListView):
	"""docstring for ReservaListView"""
	model = TipoReserva

class TipoReservaDetailView(DetailView):
	"""docstring for ReservaDetailView"""
	model= TipoReserva

class TipoReservaUpdate(UpdateView):
	"""docstring for ReservaUpdate"""
	model=TipoReserva
	fields = '__all__'

class TipoReservaCreate(CreateView):
	"""docstring for ReservaCreate"""
	model= TipoReserva
	fields = '__all__'
	
class TipoReservaDelete(DeleteView):
	"""docstring for ReservaDelete"""
	model= TipoReserva
	success_url = reverse_lazy('tiporeserva-list')
# Create your views here.
