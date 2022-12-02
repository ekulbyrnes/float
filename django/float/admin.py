from django.contrib import admin
from .models import Role, Place, Operator, Message, EmergencyPatient, EmergencyMessage
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.

admin.site.register(Role, SimpleHistoryAdmin)
admin.site.register(Place, SimpleHistoryAdmin)
admin.site.register(Operator, SimpleHistoryAdmin)
admin.site.register(Message, SimpleHistoryAdmin)
admin.site.register(EmergencyPatient, SimpleHistoryAdmin)
admin.site.register(EmergencyMessage, SimpleHistoryAdmin)