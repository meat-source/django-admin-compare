from django.contrib import admin

from django_admin_compare.admin import compare
from example.models import Car


class CarAdmin(admin.ModelAdmin):
    actions = [compare]


admin.site.register(Car, CarAdmin)
