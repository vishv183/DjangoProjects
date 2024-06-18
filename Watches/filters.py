# from django_filters import filters
# from django_filters import rest_framework as filters
# from Watches.models import Watch
#
#
# class WatchFilter(filters.FilterSet):
#     class Meta:
#         model = Watch


import django_filters
from django_filters import filters, DateTimeFilter

from Watches.models import Watch


class MyModelFilter(django_filters.FilterSet):
    created_at = filters.DateTimeFromToRangeFilter()
    start_date = DateTimeFilter(field_name="created_at", lookup_expr="gte")
    end_date = DateTimeFilter(field_name="created_at", lookup_expr="lte")

    class Meta:
        model = Watch
        fields = {
            'brand': ['in'],
            # 'created_at': ['exact', 'in', 'gt', 'lt', 'gte', 'lte'],
        }


class BaseFilter(django_filters.FilterSet):
    created_at = filters.DateTimeFromToRangeFilter()
    class Meta:
        fields = {

        }
