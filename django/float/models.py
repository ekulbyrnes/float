from django.contrib import admin
from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.

class Role(models.Model):
    id = models.BigAutoField(primary_key=True)
    history = HistoricalRecords()
    last_updated_timestamp = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.title

class Place(models.Model):
    id = models.BigAutoField(primary_key=True)
    history = HistoricalRecords()
    last_updated_timestamp = models.DateTimeField(auto_now=True)
    place = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.place

class Operator(models.Model):
    id = models.BigAutoField(primary_key=True)
    history = HistoricalRecords()
    last_updated_timestamp = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    role = models.ForeignKey('Role', blank=True, null=True, on_delete=models.SET_NULL, related_name='is_role')
    base = models.ForeignKey('Place', blank=True, null=True, on_delete=models.SET_NULL, related_name='is_base')
    command_weighting = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.name} ({self.role}): {self.base}'

class Message(models.Model):
    id = models.BigAutoField(primary_key=True)
    history = HistoricalRecords()
    last_updated_timestamp = models.DateTimeField(auto_now=True)
    message_entry_timestamp = models.DateTimeField(auto_now_add=False)
    recipient = models.ForeignKey('Operator', blank=True, null=True, on_delete=models.SET_NULL, related_name='is_recipient')
    sender = models.ForeignKey('Operator', blank=True, null=True, on_delete=models.SET_NULL, related_name='is_sender')
    current_location = models.CharField(max_length=256, null=True, blank=True)
    message_info = models.TextField(null=True)
    
    def __str__(self):
        return f'{self.id}: {self.sender} -> {self.recipient}'

class EmergencyPatient(models.Model):
    id = models.BigAutoField(primary_key=True)
    history = HistoricalRecords()
    name = models.CharField(max_length=256, null=True, default='unknown', help_text='Obtain if required for follow up after incident has been controlled.')
    age = models.IntegerField(null=True, )
    gender = models.CharField(max_length=50, null=True, )
    contact_email = models.CharField(max_length = 256, null=True, help_text='Obtain if required for follow up after incident has been controlled.')
    contact_phone = models.CharField(max_length = 20, null=True, help_text='Obtain if required for follow up after incident has been controlled.')

    def __str__(self):
        return f'{self.id}: {self.name[0]}'

class EmergencyMessage(models.Model):
    id = models.BigAutoField(primary_key=True)
    history = HistoricalRecords()
    last_updated_timestamp = models.DateTimeField(auto_now=True)
    emergency_message_entry_timestamp = models.DateTimeField(auto_now_add=False)
    event_occurance_timestamp = models.DateTimeField(auto_now_add=True)
    recipient = models.ForeignKey('Operator', blank=True, null=True, on_delete=models.SET_NULL, related_name='is_emergency_recipient')
    sender = models.ForeignKey('Operator', blank=True, null=True, on_delete=models.SET_NULL, related_name='is_emergency_sender')
    current_location = models.CharField(max_length=256, blank=True, help_text='What is the current location of the incident?')
    patient_ref = models.ForeignKey('EmergencyPatient', blank=True, null=True, on_delete=models.SET_NULL, related_name="is_patient_ref")
    cause_of_injury = models.TextField(null=True, help_text='What was the cause of the injury?')
    nature_of_injury = models.TextField(null=True, help_text='What is the nature of the injury?')
    effects_of_injury = models.TextField(null=True, help_text='What are the signs/symptoms of the injury, other observations?')
    treatment_provided = models.TextField(null=True, help_text='What treatment has been provided to the injury at this')
    
    EMERGENCY_MESSAGE_TYPE_CHOICES = [
        ('S', 'Security'),
        ('M', 'Medical'),
        ('E', 'Environmental'),
    ]
    emergency_message_type = models.CharField(
        blank=False, null=True, max_length=1, choices=EMERGENCY_MESSAGE_TYPE_CHOICES, default='M')
    
    Has_this_been_escalated = models.BooleanField(default=False)
    escalated_to = models.CharField(null = True, max_length=160)
    emergency_action = models.TextField()
    Has_this_been_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.sender} -> {self.recipient} | {self.nature_of_injury} @ {self.location} - {self.patient_ref} | Resolved: {self.Has_this_been_resolved}'

    '''
    class MessageAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'sender', 'location', 'message_info')  
    '''
