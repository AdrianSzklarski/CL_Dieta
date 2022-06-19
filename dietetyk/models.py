from django.db import models


MEAL = (
    (1, 'Filet z soli z ryżem i warzywami'),
    (2, 'Ratatouille z indyka'),
    (3, 'Sałatka z Mango i kurczakiem'),
    (4, 'Zapiekana na kurczakiem'),
    (5, 'Dorsz gotowany'),
    (6, 'Zupa pomidorowa'),
    (7, 'Leczo z piersią indyczą')

)
PRODUCT = (
    (1, 'Onion'),
    (2, 'Bread'),
    (3, 'Potato'),
    (4, 'Tomato'),
    (5, 'Salat'),
    (6, 'Chicken'),
    (7, 'Fish')
)

GRAM = (
    (1, '50 gram'),
    (2, '100 gram'),
    (3, '150 gram'),
    (4, '250 gram'),
    (5, '300 gram'),
)

SEX = (
    (1, 'male'),
    (2, 'female'),
)

class Meals(models.Model):
    """..."""
    name = models.CharField(max_length=100, unique=True)
    products = models.TextField()
    gram = models.IntegerField(choices=GRAM)

    class Meta:
        verbose_name = "Meal"
        verbose_name_plural = "Meals"

    def __str__(self):
        return self.name


class Note(models.Model):
    """..."""
    notes = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self):
        return self.notes

class Element_of_meals(models.Model):
    """..."""
    product = models.IntegerField(choices=PRODUCT)
    gram_per_100gr = models.IntegerField()

    class Meta:
        verbose_name = "Element_of_meal"
        verbose_name_plural = "Element_of_meals"

    def __str__(self):
        resum = self.get_product_display()
        return resum

class User(models.Model):
    user = models.CharField(max_length=100, unique=True)
    sex = models.IntegerField(choices=SEX)
    age = models.IntegerField()
    growth = models.IntegerField()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.user

class Dieta(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    note = models.ForeignKey('Note', on_delete=models.CASCADE, null=True)
    meals = models.ManyToManyField(Meals)
    element = models.ManyToManyField(Element_of_meals)
    user = models.ManyToManyField('User')

    class Meta:
        verbose_name = "Dieta"
        verbose_name_plural = "Dietas"

    def __str__(self):
        return self.title