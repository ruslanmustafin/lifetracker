# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 21:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('serving', models.CharField(max_length=100)),
                ('calories', models.IntegerField()),
                ('carb', models.IntegerField()),
                ('fat', models.IntegerField()),
                ('protein', models.IntegerField()),
                ('fiber', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Food'),
        ),
    ]
