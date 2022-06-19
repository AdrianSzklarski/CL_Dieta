"""Dieta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from dietetyk.views import MainPageView, MenuView, NoteView, LoginView, LogoutView, AddUserView, SendView, MealsView, \
    Element_of_mealsView, UserView, DietaView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageView.as_view(), name='main'),
    path('menu/', MenuView.as_view(), name='menu'),

    path('meals/', MealsView.as_view(), name='meals'),
    path('note/', NoteView.as_view(), name='note'),
    path('element/', Element_of_mealsView.as_view(), name='element'),
    path('user/', UserView.as_view(), name='user'),
    path('diet/', DietaView.as_view(), name='diet'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add_user/', AddUserView.as_view(), name='add-user'),

    path('send/', SendView.as_view(), name='send'),

]
