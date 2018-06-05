"""HotelesFinalFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import  url,include
from hotel import views
from rest_framework import routers
#from django.contrib.auth.decorators import login_required

router = routers.DefaultRouter()
router.register('habitacion_rest', views.HabitacionViewSet)
router.register('cliente_rest', views.ClienteViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    url(r'^$',views.base,name='base'),
    path('',views.first_view, name='first-view'),
    url(r'^habitacion/$', views.habitacion, name='habitacion-list'),
    url(r'^habitacion/(?P<habitacion_id>\d+)/detail/$', views.habitacion_detail,name='habitacion-detail'),
    # Update
    path('habitacion/<int:pk>/update/', views.HabitacionUpdate.as_view(), name='habitacion-update'),
    #Create
    path('habitacion/create/', views.HabitacionCreate.as_view(), name='habitacion-create'),
    #Delete
    path('habitacion/<int:pk>/delete/', views.HabitacionDelete.as_view(), name='habitacion-delete'),


    #Para la clase Reserva
    path('reserva/', views.ReservaListView.as_view(), name='reserva-list'),
    path('reserva/<int:pk>/detail/', views.ReservaDetailView.as_view(), name='reserva-detail'),
        # Update
    path('reserva/<int:pk>/update/', views.ReservaUpdate.as_view(), name='reserva-update'),
    #Create
    path('reserva/create/', views.ReservaCreate.as_view(), name='reserva-create'),
    #Delete
    path('reserva/<int:pk>/delete/', views.ReservaDelete.as_view(), name='reserva-delete'),

    #TIPOHABITACION
    path('tipohabitacion/', views.TipoHabitacionListView.as_view(), name='tipohabitacion-list'),
    path('tipohabitacion/<int:pk>/detail/', views.TipoHabitacionDetailView.as_view(), name='tipohabitacion-detail'),
    # Update
    path('tipohabitacion/<int:pk>/update/', views.TipoHabitacionUpdate.as_view(), name='tipohabitacion-update'),
    #Create
    path('tipohabitacion/create/', views.TipoHabitacionCreate.as_view(), name='tipohabitacion-create'),
    #Delete
    path('tipohabitacion/<int:pk>/delete/', views.TipoHabitacionDelete.as_view(), name='tipohabitacion-delete'),

    #CLIENTE
    path('cliente/', views.ClienteListView.as_view(), name='cliente-list'),
    path('cliente/<int:pk>/detail/', views.ClienteDetailView.as_view(), name='cliente-detail'),
    # Update
    path('cliente/<int:pk>/update/', views.ClienteUpdate.as_view(), name='cliente-update'),
    #Create
    path('cliente/create/', views.ClienteCreate.as_view(), name='cliente-create'),
    #Delete
    path('cliente/<int:pk>/delete/', views.ClienteDelete.as_view(), name='cliente-delete'),

    #PAGO
    path('pago/', views.PagoListView.as_view(), name='pago-list'),
    path('pago/<int:pk>/detail/', views.PagoDetailView.as_view(), name='pago-detail'),
    # Update
    path('pago/<int:pk>/update/', views.PagoUpdate.as_view(), name='pago-update'),
    #Create
    path('pago/create/', views.PagoCreate.as_view(), name='pago-create'),
    #Delete
    path('pago/<int:pk>/delete/', views.PagoDelete.as_view(), name='pago-delete'),

    #TIPO RESERVA
    path('tiporeserva/', views.TipoReservaListView.as_view(), name='tiporeserva-list'),
    path('tiporeserva/<int:pk>/detail/', views.TipoReservaDetailView.as_view(), name='tiporeserva-detail'),
    # Update
    path('tiporeserva/<int:pk>/update/', views.TipoReservaUpdate.as_view(), name='tiporeserva-update'),
    #Create
    path('tiporeserva/create/', views.TipoReservaCreate.as_view(), name='tiporeserva-create'),
    #Delete
    path('tiporeserva/<int:pk>/delete/', views.TipoReservaDelete.as_view(), name='tiporeserva-delete'),
]
