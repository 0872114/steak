from django.contrib import admin
from models import Printer


class PrinterAdmin(admin.ModelAdmin):
    pass

admin.site.register(Printer, PrinterAdmin)