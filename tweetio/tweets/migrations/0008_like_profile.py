# Generated by Django 3.0.5 on 2020-04-14 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0007_auto_20200414_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tweets.Account'),
        ),
    ]