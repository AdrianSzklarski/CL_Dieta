# Generated by Django 4.0.4 on 2022-06-15 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dietetyk', '0005_rename_product_meals_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='dieta',
            name='element',
            field=models.ManyToManyField(to='dietetyk.element_of_meals'),
        ),
        migrations.AddField(
            model_name='dieta',
            name='meals',
            field=models.ManyToManyField(to='dietetyk.meals'),
        ),
    ]
