from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from core.models import OrderStorage, OrderStatus

@receiver(pre_save, sender=OrderStorage)
def update_datafinish(sender, instance, **kwargs):
    # If the order status has changed to STORAGE
    if instance.pk is not None and instance.status == OrderStatus.STORAGE:
        # If there is a storage period specified
        if instance.period:
            if instance.period.period > 0 and instance.period.period <= 12:
                # If the start date is not specified
                if not instance.datastart:
                    instance.datastart = timezone.now()
                # Calculate the finish date
                instance.datafinish = instance.datastart + timezone.timedelta(days=instance.period.period*30)