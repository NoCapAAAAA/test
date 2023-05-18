import time

from borb.pdf import PDF
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, UpdateView, DetailView, ListView, CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from . import forms as f
import core.models as m


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
    success_url = reverse_lazy('home')
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

#
# def order_pay_tire(request, pk):
#     order = get_object_or_404(m.OrderStorage, pk=pk)
#     order.is_payed = True
#     order.save()
#     from borb.pdf import Document
from borb.pdf.page.page import Page
#
#     # Create document
#     pdf = Document()
#
#     # Add page
#     page = Page()
#     pdf.add_page(page)
#
#     from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
#     from decimal import Decimal
#
#     page_layout = SingleColumnLayout(page)
#     page_layout.vertical_margin = page.get_page_info().get_height() * Decimal(0.02)
#
#     from borb.pdf.canvas.layout.image.image import Image
#
#     page_layout.add(
#         Image(
#             "https://s3.stackabuse.com/media/articles/creating-an-invoice-in-python-with-ptext-1.png",
#             width=Decimal(128),
#             height=Decimal(128),
#         ))
#
from borb.pdf.canvas.layout.table.fixed_column_width_table import FixedColumnWidthTable as Table
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.canvas.layout.layout_element import Alignment
from datetime import datetime
import random
#
#     def _build_invoice_information():
#         table_001 = Table(number_of_rows=5, number_of_columns=3)
#
#         table_001.add(Paragraph("[Street Address]"))
#         table_001.add(Paragraph("Date", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT))
#         now = datetime.now()
#         table_001.add(Paragraph("%d/%d/%d" % (now.day, now.month, now.year)))
#
#         table_001.add(Paragraph("[City, State, ZIP Code]"))
#         table_001.add(Paragraph("Invoice #", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT))
#         table_001.add(Paragraph("%d" % random.randint(1000, 10000)))
#
#         table_001.add(Paragraph("[Phone]"))
#         table_001.add(Paragraph("Due Date", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT))
#         table_001.add(Paragraph("%d/%d/%d" % (now.day, now.month, now.year)))
#
#         table_001.add(Paragraph("[Email Address]"))
#         table_001.add(Paragraph(" "))
#         table_001.add(Paragraph(" "))
#
#         table_001.add(Paragraph("[Company Website]"))
#         table_001.add(Paragraph(" "))
#         table_001.add(Paragraph(" "))
#
#         table_001.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))
#         table_001.no_borders()
#         return table_001
#
#     page_layout = SingleColumnLayout(page)
#     page_layout.vertical_margin = page.get_page_info().get_height() * Decimal(0.02)
#     page_layout.add(
#         Image(
#             "https://s3.stackabuse.com/media/articles/creating-an-invoice-in-python-with-ptext-1.png",
#             width=Decimal(128),
#             height=Decimal(128),
#         ))
#
#     # Invoice information table
#     page_layout.add(_build_invoice_information())
#
#     # Empty paragraph for spacing
#     page_layout.add(Paragraph(" "))
from borb.pdf.canvas.color.color import HexColor, X11Color
#
#     def _build_billing_and_shipping_information():
#         table_001 = Table(number_of_rows=6, number_of_columns=2)
#         table_001.add(
#             Paragraph(
#                 "BILL TO",
#                 background_color=HexColor("263238"),
#                 font_color=X11Color("White"),
#             )
#         )
#         table_001.add(
#             Paragraph(
#                 "SHIP TO",
#                 background_color=HexColor("263238"),
#                 font_color=X11Color("White"),
#             )
#         )
#         table_001.add(Paragraph("[Recipient Name]"))  # BILLING
#         table_001.add(Paragraph("[Recipient Name]"))  # SHIPPING
#         table_001.add(Paragraph("[Company Name]"))  # BILLING
#         table_001.add(Paragraph("[Company Name]"))  # SHIPPING
#         table_001.add(Paragraph("[Street Address]"))  # BILLING
#         table_001.add(Paragraph("[Street Address]"))  # SHIPPING
#         table_001.add(Paragraph("[City, State, ZIP Code]"))  # BILLING
#         table_001.add(Paragraph("[City, State, ZIP Code]"))  # SHIPPING
#         table_001.add(Paragraph("[Phone]"))  # BILLING
#         table_001.add(Paragraph("[Phone]"))  # SHIPPING
#         table_001.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))
#         table_001.no_borders()
#         return table_001
#
#     from borb.pdf.pdf import PDF
#
#     with open("output.pdf", "wb") as pdf_file_handle:
#         PDF.dumps(pdf_file_handle, pdf)
#     return redirect(reverse_lazy('client_order_detail', kwargs={'pk': pk}))
from django.core.files import File

from io import BytesIO
from django.core.files import File
from borb.pdf import Document
from borb.pdf import SingleColumnLayout

def order_pay_tire(request, pk):
    order = get_object_or_404(m.OrderStorage, pk=pk)
    order.is_payed = True
    order.save()
    pdf = Document()
    page = Page()
    layout = SingleColumnLayout(page)

    # add a Paragraph object
    layout.add(Paragraph("Hello World!"))
    file_name = f"order_{order.pk}.pdf"
    from pathlib import Path


    with open(Path(f"\\cheuqs\\"), "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, pdf)
        time.sleep(5)
        order.cheuq.save(file_name, File(open(file_name, 'rb')))
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