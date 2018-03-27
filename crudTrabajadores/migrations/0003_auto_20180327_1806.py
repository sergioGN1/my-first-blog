# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudTrabajadores', '0002_auto_20180327_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajador',
            name='apellido',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='cargo',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
