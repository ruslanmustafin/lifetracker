from __future__ import unicode_literals

from django.db import models


class Exercise(models.Model):
    exercise_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.ForeignKey('ExerciseType', models.DO_NOTHING, db_column='type')

    class Meta:
        managed = False
        db_table = 'EXERCISE'


class ExerciseType(models.Model):
    exercise_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    unit = models.ForeignKey('Unit', models.DO_NOTHING, db_column='unit')

    class Meta:
        managed = False
        db_table = 'EXERCISE_TYPE'


class Goal(models.Model):
    goal_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user')
    type = models.IntegerField()
    amount = models.IntegerField()
    deadline_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'GOAL'


class Meal(models.Model):
    meal_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.IntegerField()
    calories = models.IntegerField(blank=True, null=True)
    protein = models.IntegerField(blank=True, null=True)
    fat = models.IntegerField(blank=True, null=True)
    carbs = models.IntegerField(blank=True, null=True)

    @staticmethod
    def get_type_name(type_number):
        meal_type_dict = {0:'food', 1:'beverage'}
        if meal_type_dict.has_key(type_number):
            return meal_type_dict[type_number]
        else:
            return 'unknown'

    class Meta:
        managed = False
        db_table = 'MEAL'


class Photo(models.Model):
    file_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='user')
    full_file_name = models.CharField(unique=True, max_length=255)
    upload_date_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'PHOTO'


class Unit(models.Model):
    unit_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'UNIT'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=32)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'USER'


class UserExerciseLink(models.Model):
    user_exercise_link_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user')
    exercise = models.ForeignKey(Exercise, models.DO_NOTHING, db_column='exercise')

    class Meta:
        managed = False
        db_table = 'USER_EXERCISE_LINK'


class UserMealLink(models.Model):
    user_meal_link_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user')
    meal = models.ForeignKey(Meal, models.DO_NOTHING, db_column='meal')
    amount = models.IntegerField(blank=True, null=True)
    meal_date_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'USER_MEAL_LINK'
