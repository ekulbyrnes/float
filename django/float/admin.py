from django.contrib import admin
from .models import Role, Place, Operator, Message, EmergencyPatient, EmergencyMessage

# Register your models here.
admin.site.register(Role)
admin.site.register(Place)
admin.site.register(Operator)
admin.site.register(Message)
admin.site.register(EmergencyPatient)
admin.site.register(EmergencyMessage)