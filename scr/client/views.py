from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from . import forms as f
import core.models as m
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


User = get_user_model()


class HomeView(TemplateView):
    template_name = 'home.html'


class AboutView(TemplateView):
    template_name = 'clientpart/about_us.html'


class ContactView(TemplateView):
    template_name = 'clientpart/contact.html'


class UserEditView(UpdateView):
    template_name = 'client_edit_profile.html'
    form_class = f.UserEditForm
    success_url = reverse_lazy('user_edit')

    def get_object(self, **kwargs):
        return self.request.user


class UserDetailView(DetailView):
    template_name = 'client_detail_profile.html'
    model = User

    def get_object(self, **kwargs):
        return self.request.user


class PasswordChangeView(UpdateView):
    form_class = f.CustomPasswordChangeForm
    template_name = 'client_password_reset.html'
    success_url = reverse_lazy('home')

    def get_object(self, **kwargs):
        return self.request.user


class OrderCreateView(LoginRequiredMixin, CreateView):

    template_name = 'client_order_create.html'
    success_url = reverse_lazy('home')
    form_class = f.OrderCreateForm
    queryset = m.OrderStorage.objects.all()

    def form_valid(self, form):
        size = int(str(form.cleaned_data['size']))
        period = int(str(form.cleaned_data['period']))
        price = size * period
        form.instance.price = price
        form.instance.user = self.request.user
        form.instance.status = m.OrderStatus.CREATE
        return super().form_valid(form)

    def get_form_kwargs(self, ):
        ret = super().get_form_kwargs()
        print(ret)
        ret['initial'] = {
            'user': self.request.user.pk,
            'status': m.OrderStatus.CREATE,
        }
        return ret


class OrderListView(LoginRequiredMixin, ListView):
    model = m.OrderStorage
    template_name = "client_order_list.html"
    context_object_name = 'orders'
    paginate_by = 5

    def get_queryset(self):
        return m.OrderStorage.objects.filter(user=self.request.user)
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['orders'] = m.OrderStorage.objects.filter(user=self.request.user)
    #     return context


class OrderDetailView(DetailView):
    template_name = "client_order_detail.html"
    model = m.OrderStorage
    extra_context = {
        'status_cancelled': m.OrderStatus.CANCELED
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detail'] = m.OrderStorage.objects.filter(pk=self.kwargs['pk'])
        return context


def order_pay_tire(request, pk):
    order = get_object_or_404(m.OrderStorage, pk=pk)
    order.is_payed = True
    order.save()
    print(order.payed_at)
    return redirect(reverse_lazy('client_order_detail', kwargs={'pk': pk}))


def order_cancel_tire(request, pk):
    order = get_object_or_404(m.OrderStorage, pk=pk)
    order.status = m.OrderStatus.CANCELED
    order.save()
    return redirect(reverse_lazy('client_order_detail', kwargs={'pk': pk}))


def cheque_tire(request, pk):
    order = get_object_or_404(m.OrderStorage, pk=pk)
    context = {
        'order': order
    }
    return render(request, 'cheque.html', context)