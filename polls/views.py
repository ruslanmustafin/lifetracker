from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Weight
from models import Meal
from models import Exercise


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

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
        weights_string += '["' + str(weight.weight_id) + '", ' + str(weight.weight_date_time.date()) + '", ' + str(
            weight.value) + ']' + ', '

    return render(request, 'weight/detail.html',
                  {'weights': weights,
                   'weightsString': weights_string[:-2]})


# def nutrition(request):
#     print UserMealLink.objects.filter(user=request.user.id).order_by('meal_date_time')
#     return render(request, 'nutrition/detail.html',
#                   {'nutrition_s': UserMealLink.objects.filter(user=request.user.id)})


def meal_list(request):
    meal_string = ''
    _nutrition = Meal.objects.filter().order_by('name')
    print _nutrition.count()
    return render(request, 'nutrition/list.html',
                  {'nutritions': _nutrition,
                   'mealString': meal_string})


def meal_by_id(request, id):
    meal_string = ''
    _nutrition = Meal.objects.filter(meal_id=id)
    for n in _nutrition:
        meal_string += str(n.protein) + ', ' + str(n.carbs) + ', ' + str(n.fat)
    print _nutrition.count()
    return render(request, 'nutrition/detail.html',
                  {'nutritions': _nutrition,
                   'mealString': meal_string})


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
    exercise_by_type = sport_to_string(Exercise.objects.filter(type=request.type.id).order_by('name'))
    return render(request, 'sport/detail.html',
                  {'exercise': exercise_by_type[:-2]})


# def user_exercises(request):
#    exercises_day = UserExerciseLink.objects.filter(user=request.user.id).order_by('name')


def sport_to_string(list):
    string = ''
    for item in list:
        string += '["' + str(item.name) + '"]\n'
    return string
