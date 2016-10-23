from django.contrib.auth.models import User, Group
from polls.models import Weight
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