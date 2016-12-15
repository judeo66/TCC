# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('RegistroData', models.DateField()),
                ('Hora', models.CharField(max_length=2, choices=[('1', 'antes do caf\xe9'), ('2', 'depois do caf\xe9'), ('3', 'antes do almo\xe7o'), ('4', 'depois do almo\xe7o'), ('5', 'antes do jantar'), ('6', 'depois do jantar'), ('7', 'Madrugada')])),
                ('NivelGlicose', models.IntegerField()),
                ('NivelCarb', models.IntegerField()),
                ('Comentario', models.CharField(max_length=255)),
                ('Unidades', models.IntegerField()),
                ('Insulina', models.CharField(max_length=1)),
                ('IdUsuario', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
