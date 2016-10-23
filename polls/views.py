from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render


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


def main(request):
    return render(request, 'main.html')


def test(request):
    return render(request, 'test.html')


@login_required(login_url='/login/')
def secured(request):
    return render(request, 'secure.html')


def test_graph(request):
    return render(request, 'test.html')


def photos(request):
    return render(request, 'photos.html')


def sport(request):
    return render(request, 'sport.html')


def weight(request):
    return render(request, 'weight.html')


def meal(request):
    return render(request, 'meal.html')
