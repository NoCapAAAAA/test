import django_filters
from core.models import OrderStorage
from django.contrib.auth import get_user_model
from authentication.models import User as AUserModel
User = get_user_model()

#Настройка фильтров


class UserFilters(django_filters.FilterSet):

    id = django_filters.CharFilter(field_name="id")

    class Meta:
        paginate_by = 7
        model = User
        fields = ('gender', 'id',)


class OrdersFilter(django_filters.FilterSet):

    id = django_filters.CharFilter(field_name="id", label='Номер заказа')

    class Meta:
        paginate_by = 7
        model = OrderStorage
        fields = ('id', 'status', 'is_payed')


class UsersFilterDirector(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name="username")

    class Meta:
        paginate_by = 7
        model = AUserModel
        fields = ('username', )
