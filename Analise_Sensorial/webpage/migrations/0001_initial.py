# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-11 21:06
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('curso', models.CharField(choices=[('A', 'Alimentos'), ('B', 'Apicultura')], default='A', max_length=1)),
                ('ano', models.CharField(choices=[('1', '1º Ano'), ('2', '2º Ano'), ('3', '3º Ano'), ('4', '4º Ano')], default='1', max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Fabricante',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Provador',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
            ],
            options={
                'verbose_name': 'Provador',
                'verbose_name_plural': 'Provadores',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Tipagem',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('tipo', models.CharField(choices=[('F', 'Fabricante'), ('P', 'Provador')], max_length=1)),
            ],
        ),
    ]
