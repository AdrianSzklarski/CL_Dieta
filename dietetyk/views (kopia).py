from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect

from dietetyk.forms import LoginForm, RegisterForm
from dietetyk.models import Meals, Note, Element_of_meals, User, Dieta
from django.contrib.auth import login, logout, authenticate

from django.shortcuts import render

from .forms import NoteAddForm

from django.contrib.auth.decorators import login_required

# klasy storny głównej
class MainPageView(View):
    def get(self, request):
        return render(request, 'Files/index.html')

class MenuView(View):
    def get(self, request):
        return render(request, 'Files/menu.html')


# Wywolanie template głównych dla podstron
# @login_required(redirect_field_name='login')
class MealsView(View):
    def get(self, request):
        textM = Meals.objects.all().order_by('name')
        return render(request, 'Files/meals.html', {'textM': textM})


# class NoteView(View):
    # def get(self, request):
    #     if request.method == 'POST':
    #         textN = Note.objects.all().order_by('notes')
    #         form = NoteAddForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('Files/menu')
    #     else:
    #         textN = NoteAddForm()
    #     return render(request, 'Files/note.html', {'textN': textN})
    # def get(self, request):
    #     textN = Note.objects.all().order_by('notes')
    #     form = NoteAddForm(instance=textN)
    #     return render(request, 'Files/note.html', {'form': form})
    #
    # def post(self, request):
    #     textN = Note.objects.all().get(name='notes') #order_by('notes')
    #     form = NoteAddForm(request.POST, instance=textN)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('Files/note.html')
class NoteView(View):
    template_name = 'Files/note.html'

    # Use the get method to pass the form to the template
    # Użyj metody get, aby przekazać formularz do szablonu
    def get(self, request, *arg, **kwargs):
        textN = NoteAddForm()

        return render(request, self.template_name, {'textN': textN})

    # Use the post method to handle the form submission
    # Użyj metody post, aby obsłużyć przesłanie formularza
    def post(self, request, *arg, **kwargs):
        # textN = Note.objects.all().order_by('notes') -> Not sure why you have this here... # -> Nie wiem, dlaczego to tu masz...
        form = NoteAddForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('Files/menu')  # Redirect upon submission # Przekieruj po przesłaniu
        else:
            print(form.errors)  # To see the field(s) preventing the form from being submitted # Aby zobaczyć pole(a) uniemożliwiające wysłanie formularza

        # Passing back the form to the template in the name 'textN'   # Przekazanie formularza z powrotem do szablonu w nazwie 'textN'
        return render(request, self.template_name, {'textN': form})


        # @login_required(redirect_field_name='login')
class Element_of_mealsView(View):
    def get(self, request):
        textE = Element_of_meals.objects.all().order_by('resume')
        return render(request, 'Files/element.html', {'textE': textE})

class UserView(View):
    def get(self, request):
        textU = User.objects.all().order_by('user')
        return render(request, 'Files/user.html', {'textU': textU})

class SendView(View):
    def get(self, request):
        return render(request, 'Files/send.html')

# @login_required(redirect_field_name='login')
class DietaView(View):
    def get(self, request):
        textD = Dieta.objects.all().order_by('title')
        return render(request, 'Files/diet.html', {'textD': textD})


# Logowanie, wylogowanie i dodanie użytkownika
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
