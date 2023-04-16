from django.views.generic import UpdateView, CreateView, TemplateView, ListView


class DirectorHomeView(TemplateView):
    template_name = 'director/home_director.html'


class DirectorCreateEmployeeView(TemplateView):
    template_name = 'director/create_employee_director.html'


class DirectorListEmployeeView(TemplateView):
    template_name = 'director/list_employee_director.html'


class DirectorOrdersReportView(TemplateView):
    template_name = 'director/orders_report_director.html'


class DirectorUsersReportView(TemplateView):
    template_name = 'director/users_report_director.html'


