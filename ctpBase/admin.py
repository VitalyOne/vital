from django.contrib import admin
from .models import Detal
from import_export import resources
from import_export.admin import ImportExportModelAdmin




#@admin.register(Detal)
class DetalAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Detal, DetalAdmin)

