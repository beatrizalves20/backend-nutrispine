# Generated by Django 5.1.2 on 2025-03-04 12:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrispine', '0005_pagamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContatoSuporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('telefone', models.CharField(max_length=14)),
                ('mensagem', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PlanoAlimentar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('telefone', models.CharField(max_length=14)),
                ('plano_alimentar', models.TextField(blank=True, null=True)),
                ('tratamento_personalizado', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prontuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diasgnostico', models.TextField()),
                ('tratamento', models.TextField()),
                ('recomendacoes', models.TextField()),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutrispine.paciente')),
            ],
        ),
    ]
