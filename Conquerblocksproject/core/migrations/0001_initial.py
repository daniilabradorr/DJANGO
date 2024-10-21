# Generated by Django 5.0.7 on 2024-08-13 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50, verbose_name="Nombre")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                (
                    "commentario",
                    models.TextField(verbose_name="Comentario que ha dejado en la web"),
                ),
            ],
        ),
    ]
