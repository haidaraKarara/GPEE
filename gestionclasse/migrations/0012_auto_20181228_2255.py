# Generated by Django 2.1.3 on 2018-12-28 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclasse', '0011_auto_20181210_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eleve',
            name='adresse',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='tuteur',
            field=models.CharField(blank=True, default='Aucun', max_length=100, verbose_name='Son/Sa tuteur/tutrice'),
        ),
    ]
