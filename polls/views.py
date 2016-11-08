from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render

from models import UserMealLink
from models import Weight
from models import ExerciseType
from models import Exercise


def login_view(request):
    return render(request, 'index-unreg.html', {})
    # return render(request, 'login.html', {})


def signup_view(request):
    return render(request, 'index-reg.html', {})


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login/')
def profile_view(request):
    return render(request, 'profile.html', {"first_name": request.user.first_name})


def auth_and_login(request, onsuccess='/profile/', onfail='/login/'):
    user = authenticate(username=request.POST['email'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect(onsuccess)
    else:
        return redirect(onfail)


def create_user(username, email, password, first_name):
    user = User(username=username, email=email, first_name=first_name)
    user.set_password(password)
    user.save()
    return user


def user_exists(username):
    user_count = User.objects.filter(username=username).count()
    if user_count == 0:
        return False
    return True


def sign_up_in(request):
    post = request.POST
    if not user_exists(post['email']):
        user = create_user(username=post['email'], email=post['email'], password=post['password'],
                           first_name=post['first_name'])
        return auth_and_login(request)
    else:
        return redirect("/login/")


def weight(request):
    weights_string = ''
    weights = Weight.objects.filter(user=request.user.id).order_by('weight_date_time')

    for weight in weights:
        weights_string += '["' + str(weight.weight_date_time.date()) + '", ' + str(weight.value) + ']' + ', '

    return render(request, 'weight/detail.html',
                  {'weights': weights,
                   'weightsString': weights_string[:-2]})


def nutrition(request):
    return render(request, 'nutrition/detail.html',
                  {'nutrition_s': UserMealLink.objects.filter(user=request.user.id)})


def main(request):
    return render(request, 'index.html')


def test(request):
    return render(request, 'test.html')


@login_required(login_url='/login/')
def secured(request):
    return render(request, 'secure.html')


def test_graph(request):
    return render(request, 'test.html')


def exercises(request):
    type_cardio = ExerciseType.objects.filter(name="cardio")
    type_force = ExerciseType.objects.filter(name="strength")
    exercises_cardio = list(Exercise.objects.filter(type=type_cardio).order_by('name'))
    exercises_force = list(Exercise.objects.filter(type=type_force).order_by('name'))
    return render(request, 'sport/detail.html',
                  {'exercises_cardio': exercises_cardio, 'exercises_force': exercises_force})


# def user_exercises(request):
#    exercises_day = UserExerciseLink.objects.filter(user=request.user.id).order_by('name')
