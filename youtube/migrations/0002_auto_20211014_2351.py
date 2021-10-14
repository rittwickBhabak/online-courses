# Generated by Django 3.2.8 on 2021-10-14 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playlist',
            old_name='github',
            new_name='github_link',
        ),
        migrations.AddField(
            model_name='playlist',
            name='google_docs_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
