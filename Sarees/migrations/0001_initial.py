# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-08 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sarees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=10)),
                ('material', models.CharField(max_length=20, null=True)),
                ('category', models.CharField(max_length=50)),
                ('colors', models.CharField(max_length=30, null=True)),
                ('size', models.CharField(max_length=20, null=True)),
                ('details', models.CharField(max_length=90, null=True)),
                ('wash', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]