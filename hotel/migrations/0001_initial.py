# Generated by Django 2.0.5 on 2018-05-22 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('identificacion', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('telefono', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaIngreso', models.DateField()),
                ('fechaSalida', models.DateField()),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotel.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='TipoHabitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='photos/')),
                ('precio', models.CharField(max_length=50)),
                ('cantidadPersonas', models.CharField(max_length=50)),
                ('idHabitacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotel.Habitacion')),
            ],
        ),
        migrations.CreateModel(
            name='TipoReserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='reserva',
            name='idTipoHabitacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotel.TipoHabitacion'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='idTipoReserva',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotel.TipoReserva'),
        ),
        migrations.AddField(
            model_name='pago',
            name='idCliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotel.Reserva'),
        ),
    ]
