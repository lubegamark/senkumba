# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-21 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0005_auto_20160721_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interesttype',
            name='type',
            field=models.CharField(choices=[('simple', 'Simple'), ('compound', 'Compound')], max_length=255),
        ),
    ]
