from django.urls import path
from .views import director as director_views
from .views import manager as manager_views

urlpatterns = [
    # Директор
    path('director/', director_views.DirectorHomeView.as_view(), name='director_home'),
    path('director/create-empl', director_views.DirectorUsersListView.as_view(), name='director_create_employee'),
    path('director/report-orders', director_views.DirectorOrdersReportView.as_view(), name='director_orders_report_view'),
    path('director/report-users', director_views.DirectorUsersReportView.as_view(), name='director_users_report_view'),
    path('director/list-empl', director_views.DirectorListEmployeeView.as_view(), name='director_list_employee_view'),

    # Менеджер
    path('manager/', manager_views.ManagerHomeView.as_view(), name='manager_home'),

    path('manager/order-crete', manager_views.ManagerCreateOrderView.as_view(), name='manager_create_order_view'),
    path('manager/order-list/', manager_views.ManagerOrdersListView.as_view(), name='manager_orders_list_view'),
    path('manager/order-list/<int:pk>/', manager_views.ManagerDetailOrderView.as_view(), name='manager_detail_order_view'),

    path('manager/create-user', manager_views.ManagerCreateUserView.as_view(), name='manager_create_user_view'),
    path('manager/user-list/', manager_views.ManagerUsersListView.as_view(), name='manager_users_list_view'),
    path('manager/user-list/<int:pk>/', manager_views.ManagerDetailUserView.as_view(), name='manager_detail_user_view'),

    # Создание контрагента
    # Создание отчёта по пользователям
    # Создание отчёта по заказам

    # path('director/users', v.DirectorUsersView.as_view(), name='directorUsers'),
    # path('director/clients', v.DirectorClientsView.as_view(), name='directorClients'),
    # path('director/stuff', v.DirectorStuffView.as_view(), name='directorStuff'),
    # path('director/orders/', v.DirectorOrdersView.as_view(), name='directorOrders'),
    # path('order_create/', v.CreateOrder.as_view(), name='create_order'),
    # path('director/orders/<int:pk>/', v.DetailOrderViewDir.as_view(), name='directorOrdersDetail'),
    #
    # path('director/create_user/', v.CreateUser.as_view(), name='create_user'),
    # path('director/statistics', v.DirectorStatisticsView.as_view(), name='directorStatistics'),
    # # path('docs/', views.TestDocument, name='report_download'),
    #
    # path('manager/', v.ManagerHomeView.as_view(), name='managerHome'),
    # path('setting/', v.ManagerEdit.as_view(), name='manager_edit'),
    # path('manager/pass/', v.PassChange.as_view(), name='pass_change'),

    # Home
    # Создание (Заказа, Пользователяб)
    # Список заказов
    # Список пользователей
    # Детальный просмотр заказа(и его редактирование)
    # Детальный просмотр пользователя(и его редактирование)
    #

]
