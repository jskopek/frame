from django.contrib import admin
from logentries_logging.models import LogentriesConnection

# Register your models here.
@admin.register(LogentriesConnection)
class LogentriesConnectionAdmin(admin.ModelAdmin):
    list_display = ('log_addr',)
