# Generated by Django 3.0.5 on 2020-04-14 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0005_auto_20200413_2213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='profile',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='tweet',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
