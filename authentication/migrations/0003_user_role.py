# Generated by Django 5.0.6 on 2024-05-22 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('ME', 'Member'), ('GU', 'Guest')], default='ME', max_length=5),
            preserve_default=False,
        ),
    ]