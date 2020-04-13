# Generated by Django 3.0.5 on 2020-04-13 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='username',
            field=models.CharField(default='default', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tweet',
            name='author',
            field=models.ForeignKey(default='default', on_delete=django.db.models.deletion.DO_NOTHING, to='tweets.Account'),
            preserve_default=False,
        ),
    ]