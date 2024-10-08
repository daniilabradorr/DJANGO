# Generated by Django 5.0.7 on 2024-08-08 19:31

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0006_alter_book_managers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-publish_date'], 'verbose_name': 'book', 'verbose_name_plural': 'books'},
        ),
        migrations.AlterModelManagers(
            name='book',
            managers=[
                ('unreturned_books', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelTable(
            name='book',
            table='book',
        ),
    ]
