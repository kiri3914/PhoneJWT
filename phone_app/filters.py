import django_filters

from .models import User
from .validators import format_phone_number_to_e164

class UserFilter(django_filters.FilterSet):
    phone_number = django_filters.CharFilter(method='filter_phone')

    class Meta:
        model = User
        fields = []

    def filter_phone(self, queryset, name, value):
        formatted_phone = format_phone_number_to_e164(value)
        if formatted_phone:
            return queryset.filter(phone_number=formatted_phone)
        return queryset.none()
