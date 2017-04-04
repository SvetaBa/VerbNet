# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 18:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VerbNet', '0002_auto_20161027_0008'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubSynset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('definition', models.CharField(max_length=300)),
                ('verb', models.CharField(max_length=30)),
                ('sample', models.CharField(max_length=300)),
                ('synonyms', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Synset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semantics', models.CharField(max_length=300)),
                ('model', models.CharField(max_length=100)),
                ('predicates', models.CharField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='Synsets',
        ),
        migrations.AddField(
            model_name='subsynset',
            name='synset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VerbNet.Synset'),
        ),
    ]
