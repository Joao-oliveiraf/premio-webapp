# Generated by Django 5.0.7 on 2024-07-23 20:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('ano', models.IntegerField()),
                ('cor', models.CharField(max_length=100)),
                ('combustivel', models.CharField(max_length=150)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('foto', models.ImageField(blank=True, upload_to='foto/%Y')),
                ('data', models.DateField(default=django.utils.timezone.now)),
                ('publicada', models.BooleanField(default=True)),
            ],
        ),
    ]
