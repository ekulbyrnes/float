from django.contrib import admin
from .models import Role, Place, Operator, Message, IncidentPatient, IncidentMessage, Incident
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.

admin.site.register(Role, SimpleHistoryAdmin)
admin.site.register(Place, SimpleHistoryAdmin)
admin.site.register(Operator, SimpleHistoryAdmin)
admin.site.register(Message, SimpleHistoryAdmin)
admin.site.register(IncidentPatient, SimpleHistoryAdmin)
admin.site.register(IncidentMessage, SimpleHistoryAdmin)
admin.site.register(Incident, SimpleHistoryAdmin)