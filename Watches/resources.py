from import_export import resources
from Watches.models import Watch


class WatchResources(resources.ModelResource):
    class Meta:
        model = Watch

    def before_save_instance(self, instance, using_transactions, dry_run):
        # Convert 'water_resistance' to integer if possible
        try:
            instance.water_resistance = int(instance.water_resistance)
        except ValueError:
            # Handle non-integer values
            pass

    def after_import_row(self, row, row_result, **kwargs):
        # Print row data for debugging
        print("aaaaaaa", row)

    def before_import(self, dataset, **kwargs):
        print('ekdfe  ferfgierfrl fef', dataset)

    def before_import_row(self, row, **kwargs):
        print('dkj jwd kferkfgerf', row)
