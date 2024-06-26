# Generated by Django 5.0.6 on 2024-05-25 17:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_alter_eventparticipation_event_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='participant',
            field=models.ManyToManyField(related_name='participants', through='schedule.EventParticipation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='eventparticipation',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_participations', to='schedule.event'),
        ),
        migrations.AlterField(
            model_name='eventparticipation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participated_events', to=settings.AUTH_USER_MODEL),
        ),
    ]
