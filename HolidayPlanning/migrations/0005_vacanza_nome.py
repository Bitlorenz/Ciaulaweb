# Generated by Django 4.2 on 2024-03-25 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HolidayPlanning', '0004_alter_vacanza_budgetdisponibile'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacanza',
            name='nome',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
