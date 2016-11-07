from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render

from models import Weight


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
    # print Weight.objects.filter(user=request.user.id)
    # user_id = request.user.id
    #
    # current_weight = Weight.objects.get(user=user_id)
    #
    # print current_weight
    # tender = form.save(commit=False)
    # tender.owner_id_id = request.user.id
    # print(request.user.id)
    # tender.save()
    # messages.success(request, 'Tender created')
    # return redirect('tenders:tenders')
    #
    weightsString = ''
    weights = Weight.objects.filter(user=request.user.id).order_by('weight_date_time')
    for weight in weights:
        weightsString += '[' + str(weight.weight_date_time.date()) + ',' + str(weight.value) + ']' + ','

    return render(request, 'weight/detail.html',
                              {'weights': weights,
                               'weightsString': weightsString[:-1]})


def main(request):
    return render(request, 'index.html')


def test(request):
    return render(request, 'test.html')


@login_required(login_url='/login/')
def secured(request):
    return render(request, 'secure.html')


def test_graph(request):
    return render(request, 'test.html')
