import time
from core.models import OrderStorage
from django.contrib import messages
from service.filters import UsersFilterDirector
from django.contrib.auth.models import Group
from organization import forms as f
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, CreateView, TemplateView, ListView
from django.contrib.auth import get_user_model, authenticate
from django.urls import reverse_lazy
from organization.forms import CreateEmployeeForm
from service.decorators import group_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.db.models.functions import ExtractYear, ExtractMonth
from django.db.models import Count
User = get_user_model()


class DirectorHomeView(TemplateView):
    @method_decorator(group_required('Директор'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    template_name = 'director/home_director.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get filter options
        grouped_purchases = OrderStorage.objects.annotate(year=ExtractYear("created_at")).values("year").order_by("-year").distinct()
        options = [purchase["year"] for purchase in grouped_purchases]
        context["filter_options"] = options

        # Get sales data for selected year
        year = self.request.GET.get("year")
        if year:
            purchases = Purchase.objects.filter(time__year=year)
            grouped_purchases = purchases.annotate(month=ExtractMonth("created_at")).values("month").annotate(count=Count("id")).values("month", "count").order_by("month")
            sales_dict = get_year_dict()
            for group in grouped_purchases:
                sales_dict[months[group["month"]-1]] = group["count"]
            context["sales_data"] = {
                "title": f"Sales in {year}",
                "data": {
                    "labels": list(sales_dict.keys()),
                    "datasets": [{
                        "label": "Number of Purchases",
                        "backgroundColor": colorPrimary,
                        "borderColor": colorPrimary,
                        "data": list(sales_dict.values()),
                    }]
                },
            }

        return context


class DirectorUsersListView(ListView):
    @method_decorator(group_required('Директор'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    template_name = 'director/users_list_director.html'
    model = User
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['filter'] = UsersFilterDirector(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self, **kwargs):
        search_results = UsersFilterDirector(self.request.GET, self.queryset)
        self.no_search_result = True if not search_results.qs else False
        return search_results.qs.distinct()


class DirectorUpdateUserView(UpdateView):
    @method_decorator(group_required('Директор'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    template_name = 'director/user_get_permissions.html'
    model = User
    form_class = f.SettingsProfile

    def get_queryset(self):
        return User.objects.filter(pk=self.kwargs['pk'])

    def form_valid(self, form):
        messages.success(self.request, "The user was updated successfully.")
        return super(DirectorUpdateUserView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('director_get_user_permissions', kwargs={'pk': self.kwargs['pk']})


class DirectorEmployeeDetailView(UpdateView):
    @method_decorator(group_required('Директор'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    template_name = 'director/detail_employee_director.html'
    model = User
    form_class = f.SettingsProfile

    def form_valid(self, form):
        user = form.save(commit=False)
        user.groups.clear()  # очищаем группы пользователя
        groups = self.request.POST.getlist('groups')  # получаем список выбранных групп
        for group_id in groups:
            group = Group.objects.get(id=group_id)
            user.groups.add(group)  # добавляем пользователя в группы
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        group_id = request.POST.get('group_id')
        if group_id:
            group = Group.objects.get(id=group_id)
            self.object.groups.remove(group)
        return super().post(request, *args, **kwargs)

    def get_queryset(self):
        return User.objects.filter(pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse_lazy('director_detail_employee_view', kwargs={'pk': self.kwargs['pk']})


class DirectorListEmployeeView(ListView):
    @method_decorator(group_required('Директор'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    template_name = 'director/list_employee_director.html'
    model = User
    paginate_by = 7
    context_object_name = 'employees'
    queryset = User.objects.filter(groups__name='Менеджер')


class DirectorOrdersReportView(TemplateView):
    @method_decorator(group_required('Директор'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    template_name = 'director/orders_report_director.html'


class DirectorUsersReportView(TemplateView):
    @method_decorator(group_required('Директор'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    template_name = 'director/users_report_director.html'


