# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-23 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('exercise_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'EXERCISE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ExerciseType',
            fields=[
                ('exercise_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'EXERCISE_TYPE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('goal_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('deadline_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'GOAL',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('meal_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('type', models.IntegerField()),
                ('calories', models.IntegerField(blank=True, null=True)),
                ('protein', models.IntegerField(blank=True, null=True)),
                ('fat', models.IntegerField(blank=True, null=True)),
                ('carbs', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'MEAL',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('file_id', models.AutoField(primary_key=True, serialize=False)),
                ('full_file_name', models.CharField(max_length=255, unique=True)),
                ('upload_date_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'PHOTO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('unit_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'UNIT',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserExerciseLink',
            fields=[
                ('user_exercise_link_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'USER_EXERCISE_LINK',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserMealLink',
            fields=[
                ('user_meal_link_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('meal_date_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'USER_MEAL_LINK',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('weight_id', models.AutoField(primary_key=True, serialize=False)),
                ('weight_date_time', models.DateTimeField()),
                ('value', models.FloatField()),
            ],
            options={
                'db_table': 'WEIGHT',
                'managed': False,
            },
        ),
        migrations.RemoveField(
            model_name='entry',
            name='food',
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
        migrations.DeleteModel(
            name='Food',
        ),
    ]