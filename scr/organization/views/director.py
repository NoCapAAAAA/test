from django.contrib.auth.models import Group
from django.views.generic import UpdateView, CreateView, TemplateView, ListView
from django.contrib.auth import get_user_model, authenticate
from django.urls import reverse_lazy
from organization.forms import CreateEmployeeForm
User = get_user_model()


class DirectorHomeView(TemplateView):
    template_name = 'director/home_director.html'


class DirectorCreateEmployeeView(CreateView):
    template_name = 'director/create_employee_director.html'
    form_class = CreateEmployeeForm
    success_url = reverse_lazy('director_list_employee_view')
    model = User

    def form_valid(self, form):
        groupe_name = str(form.cleaned_data['groups'][0])
        if groupe_name == 'Менеджер':
            group = Group.objects.get(name='Менеджер')
            self.request.user.groups.add(group)
        return super().form_valid(form)


class DirectorListEmployeeView(TemplateView):
    template_name = 'director/list_employee_director.html'


class DirectorOrdersReportView(TemplateView):
    template_name = 'director/orders_report_director.html'


class DirectorUsersReportView(TemplateView):
    template_name = 'director/users_report_director.html'


