# Generated by Django 4.0.3 on 2022-04-05 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MovieAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('release_year', models.DateField()),
                ('actor', models.ManyToManyField(to='taansen.actor')),
                ('artist', models.ManyToManyField(to='taansen.artist')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.TextField()),
                ('username', models.TextField()),
                ('user_type', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('genre', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('audio_file', models.FileField(upload_to='')),
                ('audio_link', models.CharField(max_length=200)),
                ('duration', models.CharField(max_length=20)),
                ('artist', models.ManyToManyField(to='taansen.artist')),
                ('movie_album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taansen.moviealbum')),
            ],
        ),
    ]
