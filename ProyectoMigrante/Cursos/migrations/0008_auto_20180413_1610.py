# Generated by Django 2.0.3 on 2018-04-13 23:10

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Cursos', '0007_course_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', embed_video.fields.EmbedVideoField(blank=True, default='')),
                ('nombre_unidad', models.CharField(max_length=40)),
                ('numero_unidad', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='video',
        ),
    ]