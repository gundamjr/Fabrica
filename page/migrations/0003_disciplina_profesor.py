# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20160510_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina_Profesor',
            fields=[
                ('id_Disciplina_Profesor', models.AutoField(primary_key=True, serialize=False, auto_created=True)),
                ('Disciplina_id', models.ForeignKey(to='page.Disciplina')),
                ('Professor_id', models.ForeignKey(to='page.Professor')),
            ],
        ),
    ]
