# Generated by Django 3.2.8 on 2021-10-14 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0003_ytvideo_seen_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='playlist',
            name='width',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
