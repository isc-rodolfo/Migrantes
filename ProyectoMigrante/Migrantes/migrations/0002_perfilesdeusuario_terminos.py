# Generated by Django 2.0.4 on 2018-05-04 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Migrantes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilesdeusuario',
            name='terminos',
            field=models.BooleanField(default=False),
        ),
    ]
