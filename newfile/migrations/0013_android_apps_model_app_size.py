# Generated by Django 5.0.7 on 2024-08-04 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newfile', '0012_rename_android_apps_android_apps_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='android_apps_model',
            name='app_size',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
