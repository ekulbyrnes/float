from django.db import models

# Create your models here.

class Role(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Place(models.Model):
    place = models.CharField(max_length=50)

    def __str__(self):
        return self.place

class Operator(models.Model):
    name = models.CharField(max_length=50)
    role = models.ForeignKey('Role', blank=True, null=True, on_delete=models.SET_NULL, related_name='is_role')
    base = models.ForeignKey('Place', blank=True, null=True, on_delete=models.SET_NULL, related_name='is_base')
    order = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.base} | {self.name} ({self.role})'

class Message(models.Model):
    ''' message directionality setting
    MESSAGE_DIRECTION_CHOICES = [
        ('F', 'From'),
        ('T', 'To'),
        ('B', 'Broadcast'),
    ]
    message_direction = models.CharField(
        blank=False, max_length=1, choices=MESSAGE_DIRECTION_CHOICES, default='F')
    '''
    recipient = models.ForeignKey('Operator', blank=True, null=True, on_delete=models.SET_NULL, related_name='is_recipient')
    sender = models.ForeignKey('Operator', blank=True, null=True, on_delete=models.SET_NULL, related_name='is_sender')
    location = models.CharField(max_length=256, blank=True)
    message_info = models.TextField()
    
    def __str__(self):
        return f'{self.sender} -> {self.recipient}: "{self.message_info}"'