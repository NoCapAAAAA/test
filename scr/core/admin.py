from django.contrib import admin

from . import models as m


@admin.register(m.TireSize)
class TireSize(admin.ModelAdmin):
    list_display = [field.name for field in m.TireSize._meta.fields]

    class Meta:
        model = m.TireSize




@admin.register(m.OrderStorage)
class OrderStorage(admin.ModelAdmin):
    list_display = [field.name for field in m.OrderStorage._meta.fields]

    class Meta:
        model = m.OrderStorage

    # def get_rangefilter_created_at_default(self, request):
    #     return (timezone.now().today(), timezone.now().today())
    #
    # def get_rangefilter_created_at_title(self, request, field_path):
    #     return 'Дата оформления'


@admin.register(m.PeriodOfStorage)
class PeriodOfStorage(admin.ModelAdmin):
    list_display = [field.name for field in m.PeriodOfStorage._meta.fields]

    class Meta:
        model = m.PeriodOfStorage


@admin.register(m.QuantityOfTires)
class QuantityOfTires(admin.ModelAdmin):
    list_display = [field.name for field in m.QuantityOfTires._meta.fields]

    class Meta:
        model = m.QuantityOfTires


@admin.register(m.AdressSirvice)
class AdressSirvice(admin.ModelAdmin):
    list_display = [field.name for field in m.AdressSirvice._meta.fields]

    class Meta:
        model = m.AdressSirvice


@admin.register(m.CallApplication)
class CallApplication(admin.ModelAdmin):
    list_display = [field.name for field in m.CallApplication._meta.fields]

    class Meta:
        model = m.CallApplication