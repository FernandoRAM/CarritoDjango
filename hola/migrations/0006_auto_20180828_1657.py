# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-28 21:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hola', '0005_archivo'),
    ]

    operations = [
        migrations.CreateModel(
            name='imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to='img')),
            ],
        ),
        migrations.AlterField(
            model_name='archivo',
            name='archivo',
            field=models.FileField(upload_to='doc'),
        ),
    ]
