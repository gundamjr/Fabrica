# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='matricula',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
