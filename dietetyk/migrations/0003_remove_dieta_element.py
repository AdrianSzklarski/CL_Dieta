# Generated by Django 4.0.4 on 2022-06-15 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dietetyk', '0002_element_of_meals_note_user_dieta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dieta',
            name='element',
        ),
    ]
