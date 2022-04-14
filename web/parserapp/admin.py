from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from .models import DomainModel, MxModel


@admin.register(DomainModel)
class DomainAdmin(admin.ModelAdmin, DynamicArrayMixin):
    list_display = ('id', 'url', 'domain')


@admin.register(MxModel)
class MxAdmin(admin.ModelAdmin):
    list_display = ('exchange', 'priority')
