# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-13 08:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='gallery/')),
                ('name', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('categ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='locate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo.Location'),
        ),
    ]
