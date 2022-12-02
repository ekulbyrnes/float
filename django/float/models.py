from django.contrib import admin
from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.

class Role(models.Model):
    id = models.BigAutoField(primary_key=True)
    history = HistoricalRecords()
    last_updated_timestamp = models.DateTimeField(auto_now=True, null=True) # Updates timestamp each time the object is save.
    # end of basic fields

    title = models.CharField(max_length=50, null=False,
        help_text='Role assigned for the event')

    def __str__(self):
        return self.title # returns the Role Title

class Place(models.Model):
    id = models.BigAutoField(primary_key=True)
    history = HistoricalRecords()
    last_updated_timestamp = models.DateTimeField(auto_now=True, null=True) # Updates timestamp each time the object is save.
    # end of basic fields

    place = models.CharField(max_length=50, null=False,
        help_text = 'Location assigned for the event.')

    def __str__(self):
        return self.place # returns the Place (assigned location)

class Operator(models.Model):
    id = models.BigAutoField(primary_key=True)
    history = HistoricalRecords()
    last_updated_timestamp = models.DateTimeField(auto_now=True, null=True) # Updates timestamp each time the object is save.
    # end of basic fields

    name = models.CharField(max_length=50,
        help_text='Name of the Operator.')
    role = models.ForeignKey('Role', null=True, blank=True, on_delete=models.SET_NULL, related_name='is_role', 
        help_text='Select the role of the Operator from the list.')
    base = models.ForeignKey('Place', null=True, blank=True, on_delete=models.SET_NULL, related_name='is_base',
        help_text='Select the place the Operator is assigned to from the list.')
    command_weighting = models.PositiveIntegerField(null=True,
        help_text='Provide the order in which you wish to have this operator appear in the Message dropdown.')

    def __str__(self):
        return f'{self.name} ({self.role}): {self.base}' # returns the Operator's name, role, and assigned location
        # this helps reconcile the reported location of the Operator with their assigned location and the reported 
        # location to assess if further support is required in the field.

class Message(models.Model):
    id = models.BigAutoField(primary_key=True)
    history = HistoricalRecords()
    last_updated_timestamp = models.DateTimeField(auto_now=True, null=True) # Updates timestamp each time the object is save.
    # end of basic fields

    message_entry_timestamp = models.DateTimeField(auto_now_add=False, null=True) # Records a timestamp for when the message was initially added.
    recipient = models.ForeignKey('Operator', null=True, blank=True, on_delete=models.SET_NULL, related_name='is_recipient',
        help_text='Message was received by this Operator.')
    sender = models.ForeignKey('Operator', null=True, blank=True, on_delete=models.SET_NULL, related_name='is_sender',
        help_text='Message was sent by this Operator.')
    reported_location = models.CharField(max_length=256, null=True, blank=True,
        help_text='Sender Operator\'s reported location, if provided - recipient location should be recorded if needed as message info.')
    message_info = models.TextField(null=True, blank=True,
        help_text='Message details.')
    
    def __str__(self):
        return f'{self.id}: {self.sender} -> {self.recipient}' # returns the {Message ID}: {Message Sender} -> {Message Recipient}.

class EmergencyPatient(models.Model):
    id = models.BigAutoField(primary_key=True)
    history = HistoricalRecords()
    last_updated_timestamp = models.DateTimeField(auto_now=True, null=True) # Updates timestamp each time the object is save.
    # end of basic fields

    name = models.CharField(max_length=256, null=True, blank=True, default='UNKNOWN',
        help_text='Name of the patient. Change this field once the name is known.')
    age = models.IntegerField(null=True, blank=True,
        help_text='Approximate age of patient, if known.')
    gender = models.CharField(max_length=50, null=True, blank=True,
        help_text='Reported gender of the patient, if known.')
    contact_phone = models.CharField(max_length = 20, null=True, blank=True,
        help_text='Phone is preferred - obtain if required for follow up after incident has been controlled.')
    contact_email = models.CharField(max_length = 256, null=True, blank=True,
        help_text='Obtain if required for follow up after incident has been controlled.')

    def __str__(self):
        return f'{self.id}: {self.name[0]}' # returns Patient ID: Patient's first initial - this preserves privacy on the dashboard.

class EmergencyMessage(models.Model):
    id = models.BigAutoField(primary_key=True)
    history = HistoricalRecords()
    last_updated_timestamp = models.DateTimeField(auto_now=True, null=True) # Updates timestamp each time the object is save.
    # end of basic fields

    message_entry_timestamp = models.DateTimeField(auto_now_add=False, null=True) # Creates fixed timestamp recording the message entry time.
    recipient = models.ForeignKey('Operator', null=True, blank=True, on_delete=models.SET_NULL, related_name='is_emergency_recipient',
        help_text='Message was received by this Operator.')
    sender = models.ForeignKey('Operator', null=True, blank=True, on_delete=models.SET_NULL, related_name='is_emergency_sender',
        help_text='Message was sent by this Operator.')
    # end of message transmission detail fields

    # Incident response fields
    event_occurance_timestamp = models.DateTimeField(auto_now_add=True, null=True,
        help_text='Time of the emergency events occuring') # Creates editable timestamp recording the event time.
    reported_location = models.CharField(max_length=256, null=False, blank=True, 
        help_text='What is the reported location of the incident?')
    patient_ref = models.ForeignKey('EmergencyPatient', null=True, blank=True, on_delete=models.SET_NULL, related_name="is_patient_ref",
        help_text='Create a new patient or select an existing patient to allocate a Patient ID (even if details of patient are not known at the time of the message)')
    cause_of_injury = models.TextField(null=True,
        help_text='What was the cause of the injury?')
    nature_of_injury = models.TextField(null=True,
        help_text='What is the nature of the injury?')
    effects_of_injury = models.TextField(null=True,
        help_text='What are the signs/symptoms of the injury, other observations?')
    treatment_provided = models.TextField(null=True,
        help_text='What treatment has been provided to the injury at this')
    # End of Incident response fields

    # Incident Administration fields
    EMERGENCY_MESSAGE_TYPE_CHOICES = [
        ('C', 'Child Safety'),
        ('E', 'Environmental'),
        ('M', 'Medical'),
        ('O', 'Other'),
        ('S', 'Security'),
    ]
    emergency_message_type = models.CharField(
        blank=False, null=True, max_length=1, choices=EMERGENCY_MESSAGE_TYPE_CHOICES, default='M',
        help_text='Select the nature of the emergency incident.')
    
    Has_this_been_escalated = models.BooleanField(default=False,
        help_text='Select if this incident has been delegated to another authority, as specificed below:')
    escalated_to = models.CharField(null = True, max_length=160,
        help_text='Specify a 000 department, company, custodian, etc.')
    emergency_action = models.TextField(null = True,
        help_text='Briefly explain what has been done to address the emergency situation. Provide as much detail as necessary.')
    Has_this_been_controlled = models.BooleanField(default=False,
        help_text='Select if this incident has been controlled but has yet to be resolved.')
    Has_this_been_resolved = models.BooleanField(default=False,
        help_text='Select if this incident has been resolved and no further action is required.')

    def __str__(self):
        return f'{self.id}: {self.sender} -> {self.recipient} @ {self.reported_location} ({self.patient_ref} | {self.nature_of_injury})'

# class Incident(models.Model):
#    id = models.BigAutoField(primary_key=True)
#    history = HistoricalRecords()
#    last_updated_timestamp = models.DateTimeField(auto_now=True) # Updates timestamp each time the object is save.
#    # end of basic fields 