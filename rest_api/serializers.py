from django.contrib.auth.models import User, Group
from polls.models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class WeightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Weight
        fields = ('weight_id', 'user', 'weight_date_time', 'value')


class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Exercise
		fields = ('exercise_id', 'name', 'type',)


class ExerciseLinkSerializer(serializers.HyperlinkedModelSerializer):
	exercises = ExerciseSerializer(many=True, read_only=True)

	class Meta:
		model = UserExerciseLink
		fields = ('user', 'exercises',)

class MealSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Meal
		fields = ('meal_id', 'name', 'type', 'calories', 'protein', 'fat', 'carbs',)

class MealLinkSerializer(serializers.HyperlinkedModelSerializer):
	meals = MealSerializer(many=True)

	class Meta:
		model = UserMealLink
		fields = ('user', 'meals', 'amount', 'meal_date_time',)

class UserPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPhoto
        fields = ('id', 'user', 'name', 'image',)

# class MealSerializer(serializers.HyperlinkedModelSerializer):
# 	meal = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

# 	class Meta:
# 		model = UserMealLink
# 		fields = ('user', 'exercise',)
