# Generated by Django 5.1.2 on 2024-10-17 10:27

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='tarea',
            name='fecha_completada',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tarea',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='tarea',
            name='titulo',
            field=models.CharField(default='No titulo', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarea',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
