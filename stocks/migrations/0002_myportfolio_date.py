# Generated by Django 4.0.4 on 2022-06-20 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myportfolio',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
