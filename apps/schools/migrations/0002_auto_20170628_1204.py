# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-28 06:34
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='coord',
            field=django.contrib.gis.db.models.fields.GeometryField(null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='institution',
            name='gp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='institution_gp', to='boundary.ElectionBoundary'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='last_verified_year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.AcademicYear'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='mla',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='institution_mla', to='boundary.ElectionBoundary'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='mp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='institution_mp', to='boundary.ElectionBoundary'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='ward',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='institution_ward', to='boundary.ElectionBoundary'),
        ),
    ]
