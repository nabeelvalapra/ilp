# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-22 05:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='academicyear',
            unique_together=set([('year',)]),
        ),
        migrations.AlterUniqueTogether(
            name='language',
            unique_together=set([('name',)]),
        ),
        migrations.AlterUniqueTogether(
            name='status',
            unique_together=set([('name',)]),
        ),
    ]