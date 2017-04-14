#!python
# -*- coding: utf8 -*-

from django.contrib import admin
from models import Superuser

class SuperuserAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=Superuser):
        return False

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        else:
            return True

    def has_change_permission(self, request, obj=Superuser):
        return True

admin.site.register(Superuser, SuperuserAdmin)