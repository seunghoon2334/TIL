from django.contrib import admin
from .models import Doctor, Patient

# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name']
    
class PatientAdmin(admin.ModelAdmin):
    list_display = ['name']
    
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)