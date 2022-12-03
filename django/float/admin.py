from django.contrib import admin
from .models import Role, Place, Operator, Message, IncidentPatient, Incident #, IncidentMessage,
from simple_history.admin import SimpleHistoryAdmin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
import csv

@admin.action(description='Download selected as csv')
def download_csv(modeladmin, request, queryset):
    if not request.user.is_staff:
        raise PermissionDenied
    opts = queryset.model._meta
    model = queryset.model
    response = HttpResponse(content_type='text/csv')
    # force download.
    response['Content-Disposition'] = f'attachment;filename={model._meta.model_name}.csv'
    # the csv writer
    writer = csv.writer(response)
    field_names = [field.name for field in opts.fields]
    # Write a first row with header information
    writer.writerow(field_names)
    # Write data rows
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in field_names])
    return response
admin.site.add_action(download_csv)

# Create your admin models here.

class RoleAdmin(SimpleHistoryAdmin):
    list_display = ('title',)

class PlaceAdmin(SimpleHistoryAdmin):
    list_display = ('place',)

class OperatorAdmin(SimpleHistoryAdmin):
    list_display = ('name', 'base', 'role', 'command_weighting', 'last_updated_timestamp',)
    ordering = ('command_weighting',)

class MessageAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'sender', 'recipient', 'reported_location', 'message_entry_timestamp', 'last_updated_user', 'last_updated_timestamp', 'message_info',)
    list_editable = ()
    exclude = ('last_updated_user',)

    def save_model(self, request, obj, form, change):
        obj.last_updated_user = request.user
        super().save_model(request, obj, form, change)

class IncidentPatientAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'name', 'age', 'gender', 'incident_ref', 'last_updated_timestamp',)
    list_filter = ('incident_ref',)

class IncidentAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'reported_location', 'event_occurance_timestamp', 'patient_ref', 'incident_message_type', 'nature_of_injury', 'has_this_been_escalated', 'is_incident_controlled', 'is_incident_resolved', 'last_updated_timestamp',)
    list_filter = ('reported_location', 'incident_message_type', 'patient_ref', 'has_this_been_escalated', 'is_incident_controlled', 'is_incident_resolved',)

# class IncidentMessageAdmin(SimpleHistoryAdmin):
#     list_display = ('id', 'incident_ref', 'sender', 'recipient', 'reported_location', 'message_entry_timestamp', 'last_updated_timestamp', 'message_info',)
#     list_filter = ('incident_ref',)

# Register your models here.

admin.site.register(Role, RoleAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Operator, OperatorAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(IncidentPatient, IncidentPatientAdmin)
admin.site.register(Incident, IncidentAdmin)
# admin.site.register(IncidentMessage, IncidentMessageAdmin)