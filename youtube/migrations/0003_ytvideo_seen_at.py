# Generated by Django 3.2.8 on 2021-10-14 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0002_auto_20211014_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='ytvideo',
            name='seen_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]