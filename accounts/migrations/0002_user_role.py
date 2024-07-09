# Generated by Django 5.0.6 on 2024-07-09 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('client', 'Client'), ('employee', 'Employee'), ('guest', 'Guest')], default='client', max_length=100),
        ),
    ]
