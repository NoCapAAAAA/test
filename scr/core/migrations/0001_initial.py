# Generated by Django 4.2 on 2023-04-15 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdressSirvice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=125, verbose_name='Адрес сервиса')),
            ],
            options={
                'verbose_name': 'Адрес сервиса',
                'verbose_name_plural': 'Адреса сервисов',
            },
        ),
        migrations.CreateModel(
            name='PeriodOfStorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Срок хранения',
            },
        ),
        migrations.CreateModel(
            name='QuantityOfTires',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Количество шин',
            },
        ),
        migrations.CreateModel(
            name='TireSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Диаметр шины',
                'verbose_name_plural': 'Диаметр шин',
            },
        ),
        migrations.CreateModel(
            name='OrderStorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Создан'), (1, 'На хранении'), (2, 'Отменён'), (3, 'Завершен')], default=0, verbose_name='Статус')),
                ('price', models.IntegerField(blank=True, default=0, null=True, verbose_name='Цена')),
                ('is_payed', models.BooleanField(default=False, verbose_name='Оплачен')),
                ('payed_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата оплаты')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлён')),
                ('adress', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.adresssirvice', verbose_name='Адрес')),
                ('period', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.periodofstorage', verbose_name='Период')),
                ('quantity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.quantityoftires', verbose_name='Количество')),
                ('size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.tiresize', verbose_name='Размер')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
