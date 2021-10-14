# Generated by Django 3.2.8 on 2021-10-14 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_video_last_seen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='chapter',
            name='storage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.storage'),
        ),
        migrations.AddField(
            model_name='course',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='video',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='video',
            name='is_visited',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.category'),
        ),
    ]
