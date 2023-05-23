from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core.mail import EmailMessage
from . import forms as f
import core.models as m
import os
from django.conf import settings
from service import chek_gen


User = get_user_model()


class HomeView(TemplateView):
    template_name = 'home.html'
    # Получить данные из БД по (Размер, Срок, Количество) и через JS обрабатывать по нажатию кнопки

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['size'] = m.TireSize.objects.order_by('size')
        context['quantity'] = m.QuantityOfTires.objects.order_by('quantity')
        context['period'] = m.PeriodOfStorage.objects.order_by('period')
        return context


class AboutView(TemplateView):
    template_name = 'client_about_us.html'


class ContactView(CreateView):
    template_name = 'client_contact_us.html'
    model = m.CallApplication
    success_url = reverse_lazy('home')
    fields = '__all__'


class UserEditView(UpdateView):
    template_name = 'client_edit_profile.html'
    form_class = f.UserEditForm
    success_url = reverse_lazy('client_edit_profile')

    def get_object(self, **kwargs):
        return self.request.user


class UserDetailView(DetailView):
    template_name = 'client_detail_profile.html'
    model = User

    def get_object(self, **kwargs):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_orders'] = m.OrderStorage.objects.filter(user=self.request.user).order_by('-pk')[:3]
        return context


class PasswordChangeView(UpdateView):
    form_class = f.CustomPasswordChangeForm
    template_name = 'client_password_reset.html'
    success_url = reverse_lazy('home')

    def get_object(self, **kwargs):
        return self.request.user


class OrderCreateView(LoginRequiredMixin, CreateView):

    template_name = 'client_order_create.html'
    success_url = reverse_lazy('order_success')
    form_class = f.OrderCreateForm
    queryset = m.OrderStorage.objects.all()

    def form_valid(self, form):
        if form.is_valid():
            size = int(str(form.cleaned_data['size']))
            period = int(str(form.cleaned_data['period']))
            quantity = int(str(form.cleaned_data['quantity']))
            if period * 30 > 30:
                price = size * period * quantity / 1.5
            elif period * 30 == 30:
                price = size * period * quantity

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
    check_filename = chek_gen.generate_pdf_check(order)
    order.cheque.name = check_filename
    order.save()

    # Отправка почты с вложенным PDF-чеком
    subject = 'Ваш заказ и чек'
    message = 'Спасибо за ваш заказ! Мы рады что вы выбрали именно нас! \n' \
              'Ваш чек прикреплён к данному письму'
    to_email = order.user.email

    email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [to_email])
    email.attach_file(os.path.join(settings.MEDIA_ROOT, check_filename))
    email.send()

    return redirect('order_payed')


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


def order_success(request):
    order = m.OrderStorage.objects.filter(user=request.user).order_by('-pk').first()
    context = {
        'order': order
    }
    return render(request, 'order_create_success.html', context)


def order_payed(request):
    return render(request, 'complete_payed.html')
