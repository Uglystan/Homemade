# Generated by Django 5.0.6 on 2024-05-24 18:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(blank=True, max_length=2000, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_event', models.DateTimeField()),
                ('event_type', models.CharField(choices=[('BIRTHDAY', 'Birthday'), ('MEETING', 'Meeting'), ('WORK', 'Work'), ('HOLIDAY', 'Holiday'), ('COURSE', 'Course'), ('PARTY', 'Party'), ('CULTURAL_ACTIVITY', 'Cultural activity'), ('SPORT_ACTIVITY', 'Sport activity'), ('MEDICAL', 'Medical'), ('SPECIAL', 'Special'), ('OTHER', 'Other')], max_length=17)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_authored', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventParticipation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participation', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('event', 'user')},
            },
        ),
        migrations.AddField(
            model_name='event',
            name='participant',
            field=models.ManyToManyField(related_name='participations', through='schedule.EventParticipation', to=settings.AUTH_USER_MODEL),
        ),
    ]
