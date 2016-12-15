# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cadastro', '0002_auto_20161029_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='tratamentos',
            name='Sensibilidade',
            field=models.IntegerField(default=100),
            preserve_default=True,
        ),
    ]
