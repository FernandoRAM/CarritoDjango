# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-21 05:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0002_producto_ruta'),
        ('carrito', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad', models.IntegerField()),
                ('Precio', models.IntegerField()),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrador.Producto')),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrito.Usuario')),
            ],
        ),
    ]