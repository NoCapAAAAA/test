import django_filters
from core.models import OrderStorage
from django.contrib.auth import get_user_model
User = get_user_model()
#Настройка фильтров
class UserFilters(django_filters.FilterSet):

    class Meta:
        model = User
        fields = ('gender',)