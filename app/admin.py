
import import_export
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from app.models import ComicInput

from import_export import resources
from django.db import transaction
from django.db import models


################ Include impirt/export functions for each Model ###################
class ComicInputFileAdmin(ImportExportModelAdmin):
    pass
    list_display = ("Title", "Type", "Number", "Grade","Value","CoverPic")
    list_filter = ("Title", "Grade","SellingNotes")

class ComicInputResource(resources.ModelResource):
    class Meta:
        model = ComicInput
        exclude = ('is_active',)


##################################################################
################ Admin Site Registration #########################

admin.site.register(ComicInput, ComicInputFileAdmin)