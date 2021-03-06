# Generated by Django 4.0.4 on 2022-06-15 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('product', models.IntegerField(choices=[(1, 'Filet z soli z ryżem i warzywami'), (2, 'Ratatouille z indyka'), (3, 'Sałatka z Mango i kurczakiem'), (4, 'Zapiekana na kurczakiem'), (5, 'Dorsz gotowany'), (6, 'Zupa pomidorowa'), (7, 'Leczo z piersią indyczą')])),
                ('gram', models.IntegerField(choices=[(1, '50 gram'), (2, '100 gram'), (3, '150 gram'), (4, '250 gram'), (5, '300 gram')])),
            ],
            options={
                'verbose_name': 'Meal',
                'verbose_name_plural': 'Meals',
            },
        ),
    ]
