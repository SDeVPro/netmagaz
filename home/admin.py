from django.contrib import admin
from home.models import Setting, ContactMessage
# Register your models here.
class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'update_at', 'status']
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'email', 'message', 'create_at']
    readonly_fields = ('name', 'subject', 'email', 'message', 'ip')
    list_filter = ['status']
#14.08.2020

admin.site.register(Setting, SettingAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)