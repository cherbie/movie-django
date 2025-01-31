# Generated by Django 5.0.8 on 2024-09-09 02:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('release_date', models.DateField()),
                ('genre', models.CharField(max_length=64)),
                ('runtime', models.IntegerField()),
                ('synopsis', models.TextField()),
                ('director', models.CharField(max_length=64)),
                ('rating', models.CharField(max_length=8)),
                ('princess_theatre_id', models.CharField(max_length=16)),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviehub.cinema')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MovieScreening',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('showtime', models.DateTimeField()),
                ('ticket_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviehub.cinema')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviehub.movie')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
