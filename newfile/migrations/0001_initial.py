# Generated by Django 5.0.7 on 2024-07-23 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='new_upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.TextField()),
                ('file_des', models.TextField()),
                ('file_link', models.TextField()),
                ('file_img', models.FileField(default='none', max_length=500, null='true', upload_to='')),
            ],
        ),
    ]
