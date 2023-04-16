from django.urls import path
from . import views as v

urlpatterns = [
    #Директор
    path('director/', v.DirectorHomeView.as_view(), name='directorHome'),
    # path('director/create-employee/', v.DirectorCreateEmployeeView.as_view(), name='create_director'),
    # path('director/create-report-orders/', v.DirectorCreateOrdersReport.as_view(), name='create_director'),
    # path('director/create-report-users/', v.DirectorCreateOrdersReport.as_view(), name='create_director'),

    # Создание контрагента
    # Создание отчёта по пользователям
    # Создание отчёта по заказам

    path('director/users', v.DirectorUsersView.as_view(), name='directorUsers'),
    path('director/clients', v.DirectorClientsView.as_view(), name='directorClients'),
    path('director/stuff', v.DirectorStuffView.as_view(), name='directorStuff'),
    path('director/orders/', v.DirectorOrdersView.as_view(), name='directorOrders'),
    path('order_create/', v.CreateOrder.as_view(), name='create_order'),
    path('director/orders/<int:pk>/', v.DetailOrderViewDir.as_view(), name='directorOrdersDetail'),

    path('director/create_user/', v.CreateUser.as_view(), name='create_user'),
    path('director/statistics', v.DirectorStatisticsView.as_view(), name='directorStatistics'),
    # path('docs/', views.TestDocument, name='report_download'),

    path('manager/', v.ManagerHomeView.as_view(), name='managerHome'),
    path('setting/', v.ManagerEdit.as_view(), name='manager_edit'),
    path('manager/pass/', v.PassChange.as_view(), name='pass_change'),
    """
    Менеджер todo
    """
    # Home
    # Создание (Заказа, Пользователяб)
    # Список заказов
    # Список пользователей
    # Детальный просмотр заказа(и его редактирование)
    # Детальный просмотр пользователя(и его редактирование)
    #

]
