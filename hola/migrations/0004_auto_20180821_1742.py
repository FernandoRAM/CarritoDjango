# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-21 22:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hola', '0003_prueba2_item5'),
    ]

    operations = [
        migrations.CreateModel(
            name='prueba3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='prueba2',
            name='item5',
        ),
        migrations.AddField(
            model_name='prueba3',
            name='item5',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hola.prueba2'),
        ),
    ]
