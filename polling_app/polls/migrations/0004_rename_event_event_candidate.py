# Generated by Django 4.0.4 on 2022-04-20 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_event_event'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event',
            new_name='candidate',
        ),
    ]