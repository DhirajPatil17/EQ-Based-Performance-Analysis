from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import Fyit, Syit, visualize

@admin.register(visualize)
@admin.register(Fyit)
@admin.register(Syit)


# @admin.register(Users)

class visualizeAdmin(ImportExportModelAdmin):
    list_display=('id','Name','Marks','Attendence','Behavioral')

class FyitAdmin(ImportExportModelAdmin):
    list_display=('id','Name','Marks','Attendence','Behavioral')

class SyitAdmin(ImportExportModelAdmin):
    list_display=('id','Name','Marks','Attendence','Behavioral')


