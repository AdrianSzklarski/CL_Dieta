from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views import View

from dietetyk.forms import LoginForm, RegisterForm
from dietetyk.models import Meals, Element_of_meals, User, Dieta
from django.contrib.auth import login, logout, authenticate

from django.shortcuts import render

from .forms import NoteAddForm


# homepage classes/ klasy storny głównej
class MainPageView(View):
    def get(self, request):
        return render(request, 'Files/index.html')
# homepage classes/ klasy storny głównej
class MenuView(View):
    def get(self, request):
        return render(request, 'Files/menu.html')


# Wywolanie template głównych dla podstron
@method_decorator(login_required, name='dispatch')
class MealsView(View):
    '''Meal Selection Class/ Klasa wyboru posiłków '''
    def get(self, request):
        textM = Meals.objects.all().order_by('name')
        return render(request, 'Files/meals.html', {'textM': textM})


@method_decorator(login_required, name='dispatch')
class NoteView(View):
    '''Notebook class for recording information/ Klasa notesu do zapisywania informacji'''

    template_name = 'Files/note.html'

    def get(self, request, *arg, **kwargs):
        textN = NoteAddForm()
        return render(request, self.template_name, {'textN': textN})

    def post(self, request, *arg, **kwargs):
        form = NoteAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors)
        return render(request, self.template_name, {'textN': form})


@method_decorator(login_required, name='dispatch')
class Element_of_mealsView(View):
    '''Class of meal components/ Klasa elementów składowych posiłków'''
    def get(self, request):
        textE = Element_of_meals.objects.all().order_by('resume')
        return render(request, 'Files/element.html', {'textE': textE})


@method_decorator(login_required, name='dispatch')
class UserView(View):
    '''User view class/ Klasa widoku użytkownika'''
    def get(self, request):
        textU = User.objects.all().order_by('user')
        return render(request, 'Files/user.html', {'textU': textU})


class SendView(View):
    '''Class to be used/ Klasa do wykorzytania'''
    def get(self, request):
        return render(request, 'Files/send.html')


@method_decorator(login_required, name='dispatch')
class DietaView(View):
    '''Class of dietary breakdown/ Klasa rozpisania diety'''
    def get(self, request):
        textD = Dieta.objects.all().order_by('title')
        return render(request, 'Files/diet.html', {'textD': textD})


# Logging in, logging out and adding users
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'Files/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user_login = form.cleaned_data['login']
            user_password = form.cleaned_data['password']
            user = authenticate(username=user_login, password=user_password)
            if user is None:
                return render(request, 'Files/login.html', {'form': form})
            else:
                login(request, user)
                return redirect('/menu/')
        else:
            return render(request, 'Files/login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class AddUserView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'Files/add_user.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user_login = form.cleaned_data['username']
            user_password = form.cleaned_data['pass1']
            user_first_name = form.cleaned_data['first_name']
            user_last_name = form.cleaned_data['last_name']
            user_email = form.cleaned_data['email']
            User.objects.create_user(
                username=user_login,
                password=user_password,
                first_name=user_first_name,
                last_name=user_last_name,
                email=user_email
            )
            return redirect('/login')
        else:
            return render(request, 'Files/add_user.html', {'form': form})
