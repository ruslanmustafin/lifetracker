from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_api.serializers import *
from polls.models import *
from rest_framework import generics
from django.utils.dateformat import format


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class WeightViewSet(viewsets.ModelViewSet):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer


# class WeightDateFilter(django_filters.FilterSet):
#     f = django_filters.DateTimeFilter(name="weight_date_time",lookup_type="gte")

#     class Meta:
#         model = Weight
#         fields = ['weight_date_time']


class WeightSelfViewSet(viewsets.ModelViewSet):
    serializer_class = WeightSerializer

    def get_queryset(self):
        user = self.request.user
        date_from = self.request.query_params.get('from', None)
        date_to = self.request.query_params.get('to', None)

        queryset = Weight.objects.filter(user=user)

        if date_from:
            date_from_unix = format(date_from, 'U')
            queryset = filter_date(queryset, date_from_unix)

        if date_to:
            date_to_unix = format(date_from, 'U')
            queryset = filter_date(queryset, date_to_unix, False)

        return queryset


    def filter_date(queryset, date, greater=True):
        filtered_queryset = []
        for obj in queryset:
            unix_time = format(obj.weight_date_time, 'U')
            if greater and unix_time > date:
                filtered_queryset.append(obj)
            elif not greater and unix_time < date:
                filtered_queryset.append(obj)

# class ExerciseSelfViewSet(viewsets.ModelViewSet):
#     serializer_class = ExerciseLinkSerializer

#     def get_queryset(self):
#         user = self.request.user
#         queryset = UserExerciseLink.objects.filter(user=user)
#         return queryset

# class MealSelfViewSet(viewsets.ModelViewSet):
#     serializer_class = MealLinkSerializer

#     def get_queryset(self):
#         user = self.request.user
#         queryset = UserMealLink.objects.filter(user=user)
#         return queryset


class ExerciseList(APIView):

    def get(self, request, format=None):
        user = self.request.user
        queryset = UserExerciseLink.objects.filter(user=user)
        serializer = ExerciseLinkSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        user = self.request.user
        request.data['user'] = user.id
        print request.data
        serializer = ExerciseLinkSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MealsList(APIView):

    def get(self, request, format=None):
        user = self.request.user
        queryset = UserMealLink.objects.filter(user=user)
        serializer = MealLinkSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        user = self.request.user
        request.data['user'] = user.id
        print request.data
        serializer = MealLinkSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PhotoList(APIView):

    def get(self, request, format=None):
        user = self.request.user
        photo = UserPhoto.objects.filter(user=user)
        serializer = UserPhotoSerializer(photo, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    def post(self, request, format=None):
        user = self.request.user

        request.data['user'] = user.id
        # if 'user' not in request.data:



        serializer = UserPhotoSerializer(data=request.data)
        # print request.data

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

