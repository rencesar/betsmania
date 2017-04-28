# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 06:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partidas', '0001_initial'),
        ('apostas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partidas.Match', verbose_name='Match'),
        ),
    ]
