# Generated by Django 4.0.4 on 2022-06-15 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dietetyk', '0003_remove_dieta_element'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dieta',
            name='meals',
        ),
    ]
