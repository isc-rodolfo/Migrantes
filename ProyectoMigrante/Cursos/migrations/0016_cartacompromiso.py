# Generated by Django 2.0.3 on 2018-04-22 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cursos', '0015_remove_anuncios_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartaCompromiso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('cuerpo', models.TextField()),
            ],
        ),
    ]
