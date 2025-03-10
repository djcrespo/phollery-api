# Generated by Django 5.0.6 on 2024-07-17 15:10

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('photo', models.FileField(blank=True, null=True, upload_to='photos/')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='template',
            field=models.FileField(blank=True, null=True, upload_to='templates/'),
        ),
        migrations.AddField(
            model_name='event',
            name='photos',
            field=models.ManyToManyField(related_name='event_photos', to='events.photo'),
        ),
    ]
