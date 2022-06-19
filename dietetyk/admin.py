from django.contrib import admin

from dietetyk.models import Meals, Note, Element_of_meals, User, Dieta

# Register your models here.

admin.site.register(Meals)
admin.site.register(Note)
admin.site.register(Element_of_meals)
admin.site.register(User)
admin.site.register(Dieta)