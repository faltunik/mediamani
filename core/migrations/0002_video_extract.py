# Generated by Django 4.0.4 on 2022-06-16 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video_Extract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='video/')),
                ('audio_speed', models.FileField(blank=True, null=True, upload_to='audio_extract/')),
            ],
        ),
    ]