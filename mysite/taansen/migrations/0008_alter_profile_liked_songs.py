# Generated by Django 4.0.3 on 2022-04-09 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taansen', '0007_remove_profile_song_history_profile_liked_songs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='liked_songs',
            field=models.ManyToManyField(related_name='liked_songs', to='taansen.song'),
        ),
    ]
