from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from core.models import OrderStorage

@shared_task
def check_order_conditions():
    orders = OrderStorage.objects.filter(datafinish__lte=timezone.now() + timedelta(days=5), not_finish=False)
    for order in orders:
        subject = 'Предупреждение о заказе'
        message = f'Уважаемый клиент, ваш заказ {order.pk} подходит к концу. Просьба своевременно забрать свои шины.'
        from_email = 'arttyyom@gmail.com'
        to_email = order.user.email
        send_mail(subject, message, from_email, [to_email])
        order.not_finish = True
        order.save()
