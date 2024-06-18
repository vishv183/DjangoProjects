from django.contrib import admin
from Watches.models import Watch, MyModel, Time
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from Watches.resources import WatchResources
from import_export.formats import base_formats


class WatchAdmin(ImportExportModelAdmin):
    resources = WatchResources
    list_filter = ('brand', 'price')
    def get_export_formats(self):
        """
            Returns available export formats.
            """
        formats = (
            base_formats.CSV,
            base_formats.XLS,
            base_formats.XLSX,
            base_formats.TSV,
            base_formats.ODS,
            base_formats.JSON,
            base_formats.HTML,
        )
        return [f for f in formats if f().can_export()]


admin.site.register(Watch, WatchAdmin)
admin.site.register(MyModel)
admin.site.register(Time)

