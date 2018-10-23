# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-25 23:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Correo', models.CharField(max_length=50)),
                ('Pass', models.CharField(max_length=300)),
                ('TipoUsuario', models.IntegerField()),
            ],
        ),
    ]
