# Generated by Django 3.2.8 on 2021-10-11 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('google_docs_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('google_docs_link', models.URLField()),
                ('link', models.URLField()),
                ('chapters_videos_json', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('download_page', models.URLField()),
                ('download_link', models.URLField()),
                ('last_seen', models.DateTimeField()),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.chapter')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.course'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='storage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.storage'),
        ),
    ]