# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cadastro', '0003_tratamentos_sensibilidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tratamentos',
            name='Id_medicamentoCurto',
            field=models.ForeignKey(related_name='medCurto', to='Cadastro.Medicamentos'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tratamentos',
            name='Id_medicamentoLongo',
            field=models.ForeignKey(related_name='medLongo', to='Cadastro.Medicamentos'),
            preserve_default=True,
        ),
    ]
