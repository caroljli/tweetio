# Generated by Django 3.0.5 on 2020-04-13 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_auto_20200413_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
