from core import models as m
from django.contrib import messages
from django.utils.decorators import method_decorator
from organization import forms as f
from service.filters import UserFilters, OrdersFilter
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views.generic import UpdateView, CreateView, TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from service.decorators import group_required
User = get_user_model()



class ManagerHomeView(TemplateView):
    @method_decorator(group_required('Менеджер'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    template_name = 'manager/home_manager.html'


class ManagerCreateOrderView(CreateView):
    @method_decorator(group_required('Менеджер'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    template_name = 'manager/create_order_manager.html'
    success_url = reverse_lazy('manager_orders_list_view')
    form_class = f.CreateOrderForm
    queryset = m.OrderStorage.objects.all()

    def form_valid(self, form):
        size = int(str(form.cleaned_data['size']))
        period = int(str(form.cleaned_data['period']))
        quantity = int(str(form.cleaned_data['quantity']))
        period2 = round(period*30)
        if period2 > 180:
            price = quantity * size * period2 / 1.5
            form.instance.price = price
        else:
            price = quantity * size * period2
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
    @method_decorator(group_required('Менеджер'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    template_name = 'manager/list_orders_manager.html'
    model = m.OrderStorage
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = m.OrderStorage.objects.all()
        context['filter'] = OrdersFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self, **kwargs):
        search_results = OrdersFilter(self.request.GET, self.queryset)
        self.no_search_result = True if not search_results.qs else False
        return search_results.qs.distinct()


class ManagerDetailOrderView(UpdateView):
    @method_decorator(group_required('Менеджер'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
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
    @method_decorator(group_required('Менеджер'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    template_name = 'manager/create_user_manager.html'
    success_url = reverse_lazy('manager_users_list_view')
    form_class = f.CreateUserForm


# Список пользователей с возможностью поиска по полю 'id' и филдьтрацией по полю 'gender',
# так же предусмотрена пагинация в 7 объектов
class ManagerUsersListView(ListView):
    @method_decorator(group_required('Менеджер'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    template_name = 'manager/list_users_manager.html'
    model = User
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['filter'] = UserFilters(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self, **kwargs):
        search_results = UserFilters(self.request.GET, self.queryset)
        self.no_search_result = True if not search_results.qs else False
        return search_results.qs.distinct()


class ManagerDetailUserView(UpdateView):
    @method_decorator(group_required('Менеджер'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    template_name = 'manager/detail_user_manager.html'
    model = User
    form_class = f.SettingsProfile

    def get_queryset(self):
        return User.objects.filter(pk=self.kwargs['pk'])

    def form_valid(self, form):
        messages.success(self.request, "The user was updated successfully.")
        return super(ManagerDetailUserView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('manager_detail_user_view', kwargs={'pk': self.kwargs['pk']})