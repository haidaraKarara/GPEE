# Generated by Django 2.1.3 on 2018-12-07 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclasse', '0004_auto_20181207_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eleve',
            name='tuteur',
        ),
        migrations.DeleteModel(
            name='Tuteur',
        ),
    ]