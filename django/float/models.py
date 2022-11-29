from django.contrib import admin
from django.db import models

# Create your models here.

class Role(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class RoleAdmin(admin.ModelAdmin):
    list_display = ('title')

class Place(models.Model):
    place = models.CharField(max_length=50)

    def __str__(self):
        return self.place

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('place')

class Operator(models.Model):
    name = models.CharField(max_length=50)
    role = models.ForeignKey('Role', blank=True, null=True, on_delete=models.SET_NULL, related_name='is_role')
    base = models.ForeignKey('Place', blank=True, null=True, on_delete=models.SET_NULL, related_name='is_base')
    order = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.base} | {self.name} ({self.role})'

class OperatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'base', 'order')

class Message(models.Model):
    recipient = models.ForeignKey('Operator', blank=True, null=True, on_delete=models.SET_NULL, related_name='is_recipient')
    sender = models.ForeignKey('Operator', blank=True, null=True, on_delete=models.SET_NULL, related_name='is_sender')
    location = models.CharField(max_length=256, blank=True)
    message_info = models.TextField()
    
    def __str__(self):
        return f'{self.sender} -> {self.recipient}: "{self.message_info}"'

class EmergencyPatient(models.Model):
    patient_ref = models.CharField(max_length=6, null=False)
    name = models.CharField(max_length=256, null=False)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=50, null=True)
    contact_email = models.CharField(max_length = 256, null=True)
    contact_phone = models.CharField(max_length = 20, null=True)

    def __str__(self):
        return f'{self.patient_ref}: {self.name}'

class EmergencyMessage(models.Model):
    recipient = models.ForeignKey('Operator', blank=True, null=True, on_delete=models.SET_NULL, related_name='is_emergency_recipient')
    sender = models.ForeignKey('Operator', blank=True, null=True, on_delete=models.SET_NULL, related_name='is_emergency_sender')
    location = models.CharField(max_length=256, blank=True)
    patient_ref = models.ForeignKey('EmergencyPatient', blank=True, null=True, on_delete=models.SET_NULL, related_name="is_patient_ref")
    cause_of_injury = models.TextField(null=True, help_text='What was the cause of the injury?')
    nature_of_injury = models.TextField(null=True, help_text='What is the nature of the injury?')
    effects_of_injury = models.TextField(null=True, help_text='What are the signs/symptoms of the injury, other observations?')
    Treatment_Provided = models.TextField(null=True, help_text='What treatment has been provided to the injury at this')
    
    EMERGENCY_MESSAGE_TYPE_CHOICES = [
        ('S', 'Security'),
        ('M', 'Medical'),
        ('E', 'Environmental'),
    ]
    emergency_message_type = models.CharField(
        blank=False, null=True, max_length=1, choices=EMERGENCY_MESSAGE_TYPE_CHOICES, default='M')
    
    Has_this_been_escalated = models.BooleanField(default=False)
    escalated_to = models.CharField(max_length=160)
    emergency_action = models.TextField()
    Has_this_been_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.sender} -> {self.recipient} | {self.nature_of_injury} @ {self.location} - {self.patient_ref} | Resolved: {self.Has_this_been_resolved}'

    '''
    class MessageAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'sender', 'location', 'message_info')  
    '''


'''
IMIST Situation Report:
-----------------------

(I)dentification of Patient         [using initials and Patrol number]
(M)echanism of the injury           [the cause of distress]
(I)njury/Information/Conditions     [nature of distress]
(S)igns/Symptoms and observations   [effects of injury]
(T)reatment provided                [describe if any]
'''