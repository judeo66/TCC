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
            name='Medicamentos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Marca', models.CharField(max_length=25)),
                ('Tipo', models.CharField(max_length=1, choices=[('1', 'ultrarrapida'), ('2', 'acao rapida'), ('3', 'acao intermediaria'), ('4', 'acao prolongada'), ('5', 'pre misturada regular'), ('6', 'pre misturada analoga')])),
                ('Inicio_acao', models.FloatField(max_length=1)),
                ('Pico', models.FloatField(max_length=1)),
                ('Duracao', models.FloatField(max_length=1)),
                ('Categoria', models.IntegerField(max_length=1, choices=[(1, 'Glulisina'), (2, 'Lispro'), (3, 'Asparte'), (4, 'Glargina'), (5, 'Detemir'), (6, 'Degludeca'), (7, 'NPH'), (8, 'Regular'), (9, 'Analogo bifasico'), (10, 'analogo de acao lenta'), (11, 'insulina inalavel')])),
                ('Via', models.IntegerField(max_length=1, choices=[(1, 'pouco ou nenhum exercicio fisico'), (2, 'Esporte 1-3 dias na semana'), (3, 'Esporte 3-5 dias na semana')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tratamentos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('HiperGLicemia', models.IntegerField(default=200)),
                ('HipoGlicemia', models.IntegerField(default=50)),
                ('GlicAlta', models.IntegerField(default=145)),
                ('GlicBaixa', models.IntegerField(default=80)),
                ('GLicIdeal', models.IntegerField(default=100)),
                ('Id_medicamentoCurto', models.OneToOneField(related_name='medCurto', to='Cadastro.Medicamentos')),
                ('Id_medicamentoLongo', models.OneToOneField(related_name='medLongo', to='Cadastro.Medicamentos')),
                ('Id_user', models.OneToOneField(related_name='user_trat', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('BDate', models.DateField()),
                ('Sexo', models.CharField(max_length=1)),
                ('Peso', models.IntegerField()),
                ('altura', models.IntegerField()),
                ('AtFisica', models.IntegerField(max_length=2, choices=[(1, 'pouco ou nenhum exercicio fisico'), (2, 'Esporte 1-3 dias na semana'), (3, 'Esporte 3-5 dias na semana'), (4, 'Esporte 5-7 dias na semana'), (5, 'Esporte e trabalho fisico')])),
                ('user', models.OneToOneField(related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
