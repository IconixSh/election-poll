# Generated by Django 5.2.3 on 2025-06-14 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ballot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='number_of_votes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
