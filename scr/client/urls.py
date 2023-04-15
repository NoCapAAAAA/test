from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.HomeView.as_view(), name='home'),
    path('profile/', v.UserDetailView.as_view(), name='client_detail_profile'),
    path('profile-edit/', v.UserEditView.as_view(), name='client_edit_profile'),
    path('profile-password-reset/', v.PasswordChangeView.as_view(), name='client_pass_reset'),
    path('order-create/', v.OrderCreateView.as_view(), name='client_order_create'),
    path('order-list/', v.OrderListView.as_view(), name='client_order_list'),
    path('order-list/<int:pk>/', v.OrderDetailView.as_view(), name='client_order_detail'),
    #
    path('order_pay_tire/<int:pk>/', v.order_pay_tire, name='order_pay_tire'),
    path('order_cancel_tire/<int:pk>/', v.order_cancel_tire, name='order_cancel_tire'),
    path('order_cheque_tire/<int:pk>/', v.cheque_tire, name='order_cheque_tire'),

]