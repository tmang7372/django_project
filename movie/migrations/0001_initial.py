# Generated by Django 4.0.5 on 2023-11-01 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genre', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movieId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('display', models.SmallIntegerField()),
                ('releaseDate', models.DateField()),
                ('imageUrl', models.URLField(blank=True)),
                ('active', models.CharField(max_length=1)),
                ('dateInserted', models.DateField(auto_now=True)),
                ('genreId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genre.genre')),
            ],
        ),
    ]