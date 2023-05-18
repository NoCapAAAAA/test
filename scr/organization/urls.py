from django.urls import path
from .views import director as director_views
from .views import manager as manager_views

urlpatterns = [
    # Директор
    path('director/', director_views.DirectorHomeView.as_view(), name='director_home'),
    path('director/user-list/', director_views.DirectorUsersListView.as_view(), name='director_create_employee'),
    path('director/user-list/<int:pk>/', director_views.DirectorUpdateUserView.as_view(), name='director_get_user_permissions'),
    path('director/report-orders-orders/', director_views.create_report, name='director_orders_report_view'),
    path('director/report-orders-users/', director_views.create_report_users, name='director_users_report_view'),
    path('director/list-empl/', director_views.DirectorListEmployeeView.as_view(), name='director_list_employee_view'),
    path('director/list-empl/<int:pk>/', director_views.DirectorEmployeeDetailView.as_view(), name='director_detail_employee_view'),
    path('director/user-list/', director_views.DirectorUsersListView.as_view(), name='director_create_employee'),
    path('director/user-list/', director_views.DirectorUsersListView.as_view(), name='director_create_employee'),
    path('director/user-list/', director_views.DirectorUsersListView.as_view(), name='director_create_employee'),
    # Test
    path("director/filter-options/", director_views.get_filter_options, name="chart-filter-options"),
    path("director/<int:year>/", director_views.get_sales_chart, name="chart-sales"),

    # Менеджер
    path('manager/', manager_views.ManagerHomeView.as_view(), name='manager_home'),
    path('manager/order-crete', manager_views.ManagerCreateOrderView.as_view(), name='manager_create_order_view'),
    path('manager/order-list/', manager_views.ManagerOrdersListView.as_view(), name='manager_orders_list_view'),
    path('manager/order-list/<int:pk>/', manager_views.ManagerDetailOrderView.as_view(), name='manager_detail_order_view'),
    path('manager/create-user', manager_views.ManagerCreateUserView.as_view(), name='manager_create_user_view'),
    path('manager/user-list/', manager_views.ManagerUsersListView.as_view(), name='manager_users_list_view'),
    path('manager/user-list/<int:pk>/', manager_views.ManagerDetailUserView.as_view(), name='manager_detail_user_view'),

]
