# Generated by Django 5.0.6 on 2024-07-09 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0002_logs_date_created'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Logs',
            new_name='Log',
        ),
    ]
