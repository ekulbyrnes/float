# Generated by Django 4.1.3 on 2022-12-02 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('float', '0010_historicalincidentmessage_reported_location_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalincident',
            old_name='incident_action',
            new_name='action_taken',
        ),
        migrations.RenameField(
            model_name='incident',
            old_name='incident_action',
            new_name='action_taken',
        ),
    ]