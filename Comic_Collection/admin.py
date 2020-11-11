# Regist
# er your models here;
import import_export
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from django.contrib import admin
from .models import ComicInput
from import_export import resources


################ Include impirt/export functions for each Model ###################
class ComicInputFileAdmin(ImportExportModelAdmin):
    pass


class ComicInputResource(resources.ModelResource):
    class Meta:
        model = ComicInput
        exclude = ('is_active',)


##################################################################
################ Admin Site Registration #########################

admin.site.register(ComicInput, ComicInputFileAdmin)