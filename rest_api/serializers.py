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

class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = ('weight_id', 'user', 'weight_date_time', 'value')


class ExerciseUnitSerializer(serializers.ModelSerializer):
	class Meta:
		model = Unit
		fields = ('name',)
			

class ExerciseTypeSerializer(serializers.ModelSerializer):

	unit = ExerciseUnitSerializer()

	class Meta:
		model = ExerciseType
		fields = ('name', 'unit')

class ExerciseSerializer(serializers.ModelSerializer):
	type = ExerciseTypeSerializer()

	class Meta:
		model = Exercise
		fields = ('name', 'type')


class ExerciseLinkSerializer(serializers.ModelSerializer):
	exercise = ExerciseSerializer()

	class Meta:
		model = UserExerciseLink
		fields = ('user', 'exercise', 'value')

	def create(self, validated_data):
		exercise = validated_data.pop('exercise')

		user = validated_data.pop('user')
		value = validated_data.pop('value')

		ex_type = ExerciseType.objects.filter(name=exercise['type']['name'])
		print ex_type[0]
		exercise['type'] = ex_type[0]

		exer_obj = Exercise.objects.create(**exercise)
		usel_obj = UserExerciseLink.objects.create(user=user, exercise=exer_obj, value=value)
		return usel_obj

class MealSerializer(serializers.ModelSerializer):
	class Meta:
		model = Meal
		fields = ('name', 'type', 'calories', 'protein', 'fat', 'carbs',)

class MealLinkSerializer(serializers.ModelSerializer):
	meal = MealSerializer()

	class Meta:
		model = UserMealLink
		fields = ('user', 'meal', 'amount', 'meal_date_time',)

	def create(self, validated_data):
		meal = validated_data.pop('meal')
		user = validated_data.pop('user')
		amount = validated_data.pop('amount')
		meal_date_time = validated_data.pop('meal_date_time')

		meal_obj = Meal.objects.create(**meal)
		usml_obj = UserMealLink.objects.create(user=user, meal=meal_obj, amount=amount, meal_date_time=meal_date_time)
		return usml_obj

class UserPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPhoto
        fields = ('id', 'user', 'name', 'image',)

# class MealSerializer(serializers.HyperlinkedModelSerializer):
# 	meal = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

# 	class Meta:
# 		model = UserMealLink
# 		fields = ('user', 'exercise',)
