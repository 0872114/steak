#!python
# -*- coding: utf8 -*-

from django.contrib import admin
from models import Printer, Categories, Tags


class PrinterAdmin(admin.ModelAdmin):
    pass

admin.site.register(Printer, PrinterAdmin)


class CategoriesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Categories, CategoriesAdmin)


class TagsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tags, TagsAdmin)
