# Generated by Django 4.1.3 on 2022-12-03 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('float', '0017_alter_operator_options_historicaloperator_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='security',
            options={'ordering': ('callsign', 'name')},
        ),
        migrations.AddField(
            model_name='historicaloperator',
            name='callsign',
            field=models.CharField(blank=True, help_text='Callsign of the Operator.', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='operator',
            name='callsign',
            field=models.CharField(blank=True, help_text='Callsign of the Operator.', max_length=50, null=True),
        ),
    ]