# Generated by Django 3.0.7 on 2020-06-20 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('identifier', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Profesor',
                'verbose_name_plural': 'Profesores',
                'ordering': ['name'],
            },
        ),
    ]
