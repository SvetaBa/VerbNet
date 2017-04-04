# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VerbNet', '0003_auto_20161212_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsynset',
            name='definition',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='subsynset',
            name='sample',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='subsynset',
            name='synonyms',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='subsynset',
            name='verb',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='synset',
            name='model',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='synset',
            name='predicates',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='synset',
            name='semantics',
            field=models.CharField(max_length=300, null=True),
        ),
    ]