from django.utils import timezone
from celery import shared_task
from django.core.mail import send_mail
from core.models import OrderStorage
from django.conf import settings


@shared_task
def check_order_storage():
    # Получение всех записей из таблицы OrderStorage
    orders = OrderStorage.objects.all()

    for order in orders:
        # Проверка, что дата окончания хранения меньше или равна 5 дням
        if order.datafinish and (order.datafinish - timezone.now()).days <= 5:
            # Проверка, что письмо не было отправлено ранее
            if not order.email_sent:
                # Отправка письма на почту пользователя
                send_mail(
                    'Важное уведомление',
                    'Ваше хранилище истекает через 5 дней!',
                    settings.EMAIL_HOST_USER,  # Отправитель
                    [order.user.email],  # Получатель
                    fail_silently=False,
                )
                # Установка флага, что письмо было отправлено
                order.email_sent = True
                order.save()
