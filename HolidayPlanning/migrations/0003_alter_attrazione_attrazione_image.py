# Generated by Django 4.2 on 2023-10-30 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HolidayPlanning', '0002_attrazione_attrazione_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attrazione',
            name='attrazione_image',
            field=models.ImageField(blank=True, null=True, upload_to='attractionImages'),
        ),
    ]