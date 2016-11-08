"""lifetracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import url, include

from django.contrib import admin
from polls import views as polls_views

from rest_framework import routers
from rest_api import views as rest_views

router = routers.DefaultRouter()
router.register(r'users', rest_views.UserViewSet)
router.register(r'groups', rest_views.GroupViewSet)
# router.register(r'weight', rest_views.WeightViewSet)
# router.register(r'photo', rest_views.PhotoList.as_view(), base_name='userphoto-list')
router.register(r'weight', rest_views.WeightSelfViewSet, base_name='weight-list')
router.register(r'exercises', rest_views.ExerciseSelfViewSet, base_name='exercises-list')
router.register(r'meals', rest_views.MealSelfViewSet, base_name='meals-list')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', polls_views.login_view),
    url(r'^sign-up/', polls_views.signup_view),
    url(r'^logout/', polls_views.logout_view),
    url(r'^auth/', polls_views.auth_and_login),
    url(r'^signup/', polls_views.sign_up_in),
    url(r'^profile/', polls_views.profile_view),
    url(r'^$', polls_views.main),
    url(r'^test_graph/', polls_views.test_graph),
    url(r'^api/', include(router.urls)),
    url(r'^api/photo/$', rest_views.PhotoList.as_view(), name='myphoto-list'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
