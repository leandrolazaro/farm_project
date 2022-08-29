from django_filters import FilterSet, filters

from farm_base.api.v1.filters.fields import NumberInFilter
from farm_base.models import Farm, Owner


class FarmFilter(FilterSet):
    # ids = NumberInFilter(field_name='id', lookup_expr='in')

    class Meta:
        model = Farm
        fields = ['id', 'name', 'owner__name', 'owner__id', 'owner__document', 'municipality', 'state']
