# Generated by Django 4.1.3 on 2022-12-03 01:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    replaces = [('float', '0001_initial'), ('float', '0002_message_recipient_message_sender'), ('float', '0003_rename_message_location_message_location'), ('float', '0004_emergencypatient_emergencymessage'), ('float', '0005_alter_emergencymessage_patient_ref'), ('float', '0006_alter_emergencymessage_escalated_to_historicalrole_and_more'), ('float', '0007_rename_treatment_provided_emergencymessage_treatment_provided_and_more'), ('float', '0008_historicalincident_historicalincidentmessage_and_more'), ('float', '0009_historicalincidentmessage_incident_ref_and_more'), ('float', '0010_historicalincidentmessage_reported_location_and_more'), ('float', '0011_rename_incident_action_historicalincident_action_taken_and_more'), ('float', '0012_rename_has_this_been_escalated_historicalincident_has_this_been_escalated_and_more'), ('float', '0013_remove_incidentmessage_incident_ref_and_more'), ('float', '0014_alter_historicalmessage_incident_ref_and_more'), ('float', '0015_historicalmessage_last_updated_user_and_more')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('place', models.CharField(help_text='Location assigned for the event.', max_length=50)),
                ('last_updated_timestamp', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='Role assigned for the event', max_length=50)),
                ('last_updated_timestamp', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name of the Operator.', max_length=50)),
                ('base', models.ForeignKey(blank=True, help_text='Select the place the Operator is assigned to from the list.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='is_base', to='float.place')),
                ('role', models.ForeignKey(blank=True, help_text='Select the role of the Operator from the list.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='is_role', to='float.role')),
                ('command_weighting', models.PositiveIntegerField(help_text='Provide the order in which you wish to have this operator appear in the Message dropdown.', null=True)),
                ('last_updated_timestamp', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IncidentPatient',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='UNKNOWN', help_text='Name of the patient. Change this field once the name is known.', max_length=256, null=True)),
                ('age', models.IntegerField(blank=True, help_text='Approximate age of patient, if known.', null=True)),
                ('gender', models.CharField(blank=True, help_text='Reported gender of the patient, if known.', max_length=50, null=True)),
                ('contact_email', models.CharField(blank=True, help_text='Obtain if required for follow up after incident has been controlled.', max_length=256, null=True)),
                ('contact_phone', models.CharField(blank=True, help_text='Phone is preferred - obtain if required for follow up after incident has been controlled.', max_length=20, null=True)),
                ('last_updated_timestamp', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalOperator',
            fields=[
                ('id', models.BigIntegerField(blank=True, db_index=True)),
                ('name', models.CharField(help_text='Name of the Operator.', max_length=50)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('base', models.ForeignKey(blank=True, db_constraint=False, help_text='Select the place the Operator is assigned to from the list.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='float.place')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('role', models.ForeignKey(blank=True, db_constraint=False, help_text='Select the role of the Operator from the list.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='float.role')),
                ('command_weighting', models.PositiveIntegerField(help_text='Provide the order in which you wish to have this operator appear in the Message dropdown.', null=True)),
                ('last_updated_timestamp', models.DateTimeField(blank=True, editable=False, null=True)),
            ],
            options={
                'verbose_name': 'historical operator',
                'verbose_name_plural': 'historical operators',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPlace',
            fields=[
                ('id', models.BigIntegerField(blank=True, db_index=True)),
                ('place', models.CharField(help_text='Location assigned for the event.', max_length=50)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('last_updated_timestamp', models.DateTimeField(blank=True, editable=False, null=True)),
            ],
            options={
                'verbose_name': 'historical place',
                'verbose_name_plural': 'historical places',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalRole',
            fields=[
                ('id', models.BigIntegerField(blank=True, db_index=True)),
                ('title', models.CharField(help_text='Role assigned for the event', max_length=50)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('last_updated_timestamp', models.DateTimeField(blank=True, editable=False, null=True)),
            ],
            options={
                'verbose_name': 'historical role',
                'verbose_name_plural': 'historical roles',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalIncident',
            fields=[
                ('id', models.BigIntegerField(blank=True, db_index=True)),
                ('last_updated_timestamp', models.DateTimeField(blank=True, editable=False)),
                ('event_occurance_timestamp', models.DateTimeField(blank=True, editable=False, help_text='Time of the incident events occuring', null=True)),
                ('reported_location', models.CharField(blank=True, help_text='What is the reported location of the incident?', max_length=256)),
                ('cause_of_injury', models.TextField(help_text='What was the cause of the injury?', null=True)),
                ('nature_of_injury', models.TextField(help_text='What is the nature of the injury?', null=True)),
                ('effects_of_injury', models.TextField(help_text='What are the signs/symptoms of the injury, other observations?', null=True)),
                ('treatment_provided', models.TextField(help_text='What treatment has been provided to the injury at this', null=True)),
                ('incident_message_type', models.CharField(choices=[('C', 'Child Safety - missing, endangered, threatened, etc'), ('E', 'Environmental - location or structure based issues.'), ('M', 'Medical - injuries and illness of people involved in the event.'), ('O', 'Operational - preventing the effective execution of the event.'), ('S', 'Security - threats to people involved in the event.'), ('U', 'Undefined threats to the event.')], default='M', help_text='Select the nature of the incident.', max_length=1, null=True)),
                ('has_this_been_escalated', models.BooleanField(default=False, help_text='Select if this incident has been delegated to another authority, as specificed below:')),
                ('escalated_to', models.CharField(help_text='Specify a 000 department, company, custodian, etc.', max_length=160, null=True)),
                ('action_taken', models.TextField(help_text='Briefly explain what has been done to address the incident situation. Provide as much detail as necessary.', null=True)),
                ('is_incident_controlled', models.BooleanField(default=False, help_text='Select if this incident has been controlled but has yet to be resolved.')),
                ('is_incident_resolved', models.BooleanField(default=False, help_text='Select if this incident has been resolved and no further action is required.')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('patient_ref', models.ForeignKey(blank=True, db_constraint=False, help_text='Create a new patient or select an existing patient to allocate a Patient ID (even if details of patient are not known at the time of the message)', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='float.incidentpatient')),
            ],
            options={
                'verbose_name': 'historical incident',
                'verbose_name_plural': 'historical incidents',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('last_updated_timestamp', models.DateTimeField(auto_now=True)),
                ('event_occurance_timestamp', models.DateTimeField(auto_now_add=True, help_text='Time of the incident events occuring', null=True)),
                ('reported_location', models.CharField(blank=True, help_text='What is the reported location of the incident?', max_length=256)),
                ('cause_of_injury', models.TextField(help_text='What was the cause of the injury?', null=True)),
                ('nature_of_injury', models.TextField(help_text='What is the nature of the injury?', null=True)),
                ('effects_of_injury', models.TextField(help_text='What are the signs/symptoms of the injury, other observations?', null=True)),
                ('treatment_provided', models.TextField(help_text='What treatment has been provided to the injury at this', null=True)),
                ('incident_message_type', models.CharField(choices=[('C', 'Child Safety'), ('E', 'Environmental'), ('M', 'Medical'), ('O', 'Other'), ('S', 'Security')], default='M', help_text='Select the nature of the incident.', max_length=1, null=True)),
                ('Has_this_been_escalated', models.BooleanField(default=False, help_text='Select if this incident has been delegated to another authority, as specificed below:')),
                ('escalated_to', models.CharField(help_text='Specify a 000 department, company, custodian, etc.', max_length=160, null=True)),
                ('incident_action', models.TextField(help_text='Briefly explain what has been done to address the incident situation. Provide as much detail as necessary.', null=True)),
                ('Has_this_been_controlled', models.BooleanField(default=False, help_text='Select if this incident has been controlled but has yet to be resolved.')),
                ('Has_this_been_resolved', models.BooleanField(default=False, help_text='Select if this incident has been resolved and no further action is required.')),
                ('patient_ref', models.ForeignKey(blank=True, help_text='Create a new patient or select an existing patient to allocate a Patient ID (even if details of patient are not known at the time of the message)', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='is_patient_ref', to='float.incidentpatient')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalIncidentPatient',
            fields=[
                ('id', models.BigIntegerField(blank=True, db_index=True)),
                ('name', models.CharField(blank=True, default='UNKNOWN', help_text='Name of the patient. Change this field once the name is known.', max_length=256, null=True)),
                ('age', models.IntegerField(blank=True, help_text='Approximate age of patient, if known.', null=True)),
                ('gender', models.CharField(blank=True, help_text='Reported gender of the patient, if known.', max_length=50, null=True)),
                ('contact_email', models.CharField(blank=True, help_text='Obtain if required for follow up after incident has been controlled.', max_length=256, null=True)),
                ('contact_phone', models.CharField(blank=True, help_text='Phone is preferred - obtain if required for follow up after incident has been controlled.', max_length=20, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('last_updated_timestamp', models.DateTimeField(blank=True, editable=False, null=True)),
                ('incident_ref', models.ForeignKey(blank=True, db_constraint=False, help_text='Create a new patient or select an existing patient to allocate a Patient ID (even if details of patient are not known at the time of the message)', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='float.incident')),
            ],
            options={
                'verbose_name': 'historical incident patient',
                'verbose_name_plural': 'historical incident patients',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddField(
            model_name='incidentpatient',
            name='incident_ref',
            field=models.ForeignKey(blank=True, help_text='Create a new patient or select an existing patient to allocate a Patient ID (even if details of patient are not known at the time of the message)', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='is_incident_ref', to='float.incident'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='patient_ref',
            field=models.ForeignKey(blank=True, help_text='Create a new patient or select an existing patient to allocate a Patient ID (even if details of patient are not known at the time of the message)', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='is_incidentpatient_ref', to='float.incidentpatient'),
        ),
        migrations.RenameField(
            model_name='incident',
            old_name='incident_action',
            new_name='action_taken',
        ),
        migrations.RenameField(
            model_name='incident',
            old_name='Has_this_been_escalated',
            new_name='has_this_been_escalated',
        ),
        migrations.RenameField(
            model_name='incident',
            old_name='Has_this_been_controlled',
            new_name='is_incident_controlled',
        ),
        migrations.RenameField(
            model_name='incident',
            old_name='Has_this_been_resolved',
            new_name='is_incident_resolved',
        ),
        migrations.CreateModel(
            name='HistoricalMessage',
            fields=[
                ('id', models.BigIntegerField(blank=True, db_index=True)),
                ('message_info', models.TextField(blank=True, help_text='Message details.', null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('recipient', models.ForeignKey(blank=True, db_constraint=False, help_text='Message was received by this Operator.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='float.operator')),
                ('sender', models.ForeignKey(blank=True, db_constraint=False, help_text='Message was sent by this Operator.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='float.operator')),
                ('last_updated_timestamp', models.DateTimeField(blank=True, editable=False, null=True)),
                ('message_entry_timestamp', models.DateTimeField(null=True)),
                ('reported_location', models.CharField(blank=True, help_text="Sender Operator's reported location, if provided - recipient location should be recorded if needed as message info.", max_length=256, null=True)),
                ('incident_ref', models.ForeignKey(blank=True, db_constraint=False, help_text='Create a new incident or select an existing incident.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='float.incident')),
                ('last_updated_user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical message',
                'verbose_name_plural': 'historical messages',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('message_info', models.TextField(blank=True, help_text='Message details.', null=True)),
                ('recipient', models.ForeignKey(blank=True, help_text='Message was received by this Operator.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='is_recipient', to='float.operator')),
                ('sender', models.ForeignKey(blank=True, help_text='Message was sent by this Operator.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='is_sender', to='float.operator')),
                ('last_updated_timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('message_entry_timestamp', models.DateTimeField(null=True)),
                ('reported_location', models.CharField(blank=True, help_text="Sender Operator's reported location, if provided - recipient location should be recorded if needed as message info.", max_length=256, null=True)),
                ('incident_ref', models.ForeignKey(blank=True, help_text='Create a new incident or select an existing incident.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='is_incidentmessage_ref', to='float.incident')),
                ('last_updated_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='incident',
            name='incident_message_type',
            field=models.CharField(choices=[('C', 'Child Safety - missing, endangered, threatened, etc'), ('E', 'Environmental - location or structure based issues.'), ('M', 'Medical - injuries and illness of people involved in the event.'), ('O', 'Operational - preventing the effective execution of the event.'), ('S', 'Security - threats to people involved in the event.'), ('U', 'Undefined threats to the event.')], default='M', help_text='Select the nature of the incident.', max_length=1, null=True),
        ),
    ]
