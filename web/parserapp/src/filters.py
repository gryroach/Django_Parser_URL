from django_filters import rest_framework as filters
from ..models import DomainModel


class DomainFilter(filters.FilterSet):
    start_create_date = filters.DateFilter(field_name='create_date', lookup_expr='gt')
    end_create_date = filters.DateFilter(field_name='create_date', lookup_expr='lt')

    class Meta:
        model = DomainModel
        fields = ['url', 'domain', 'country', 'isDead']
