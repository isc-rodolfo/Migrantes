# Generated by Django 2.0.3 on 2018-04-12 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cursos', '0002_auto_20180412_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='estudiante',
            field=models.ManyToManyField(null=True, to='Migrantes.PerfilesDeUsuario'),
        ),
    ]
