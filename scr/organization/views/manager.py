import datetime
from core import models as m
from django.utils import timezone
from django.contrib import messages
from organization import forms as f
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views.generic import UpdateView, CreateView, TemplateView, ListView, DetailView


User = get_user_model()

class ManagerHomeView(TemplateView):
    template_name = 'manager/home_manager.html'


class ManagerCreateOrderView(CreateView):
    template_name = 'manager/create_order_manager.html'
    success_url = reverse_lazy('manager_orders_list_view')
    form_class = f.CreateOrderForm
    queryset = m.OrderStorage.objects.all()

    def form_valid(self, form):
        size = int(str(form.cleaned_data['size']))
        period = int(str(form.cleaned_data['period']))
        price = size * period
        form.instance.price = price
        form.instance.status = m.OrderStatus.CREATE
        return super().form_valid(form)

    def get_form_kwargs(self, ):
        ret = super().get_form_kwargs()
        ret['initial'] = {
            'status': m.OrderStatus.CREATE,
        }
        return ret


class ManagerOrdersListView(ListView):
    template_name = 'manager/list_orders_manager.html'
    model = m.OrderStorage
    context_object_name = 'orders'
    paginate_by = 7

    @staticmethod
    def get_date_range_default():
        date1 = timezone.now()
        date2 = timezone.now()
        return date1, date2

    def get_date_range(self):
        strptime = datetime.datetime.strptime
        try:
            date1 = (strptime(self.request.GET.get('date_from'), r'%Y-%m-%d'))
            date2 = (strptime(self.request.GET.get('date_until'), r'%Y-%m-%d'))
        except TypeError:
            date1, date2 = self.get_date_range_default()

        if date1 > date2:
            date1, date2 = date2, date1
        return date1, date2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date1, date2 = self.get_date_range()
        context['date_from'], context['date_until'] = (
            date1.strftime(r'%Y-%m-%d'), date2.strftime(r'%Y-%m-%d'))
        context['today'] = timezone.now()
        return context

    def get_queryset(self):
        queryset = m.OrderStorage.objects.all().order_by('-pk')
        date_from, date_until = self.get_date_range()
        queryset = queryset.filter(
            created_at__gte=datetime.datetime.combine(date_from, datetime.time.min),
            created_at__lte=datetime.datetime.combine(date_until, datetime.time.max)
        )
        return queryset


class ManagerDetailOrderView(UpdateView):
    template_name = 'manager/detail_order_manager.html'
    model = m.OrderStorage
    form_class = f.UpdateOrderDir

    def get_queryset(self):
        return m.OrderStorage.objects.filter(pk=self.kwargs['pk'])

    def form_valid(self, form):
        messages.success(self.request, "The task was updated successfully.")
        return super(ManagerDetailOrderView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('manager_detail_order_view', kwargs={'pk': self.kwargs['pk']})


class ManagerCreateUserView(CreateView):
    template_name = 'manager/create_user_manager.html'
    success_url = reverse_lazy('manager_users_list_view')
    form_class = f.CreateUserForm


class ManagerUsersListView(ListView):
    template_name = 'manager/list_users_manager.html'
    model = User
    paginate_by = 7
    context_object_name = 'users'


class ManagerDetailUserView(TemplateView):
    template_name = 'manager/detail_user_manager.html'
