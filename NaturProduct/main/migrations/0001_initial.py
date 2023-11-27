# Generated by Django 4.2.7 on 2023-11-28 07:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderId', models.IntegerField(primary_key=True, serialize=False)),
                ('orderDate', models.DateField(default=django.utils.timezone.now)),
                ('orderAddress', models.TextField(max_length=50)),
                ('orderCost', models.IntegerField()),
                ('orderPhoneNumber', models.IntegerField()),
                ('orderPayment', models.TextField(choices=[('ОН', 'Онлайн оплата'), ('КП', 'Картой при получении'), ('НП', 'Наличными при получении')])),
                ('orderStatus', models.TextField(choices=[('ОП', 'Оплачен'), ('СЗ', 'Сбор заказа'), ('ДС', 'Доставка курьером'), ('ДО', 'Доставлен')])),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('OPId', models.IntegerField(primary_key=True, serialize=False)),
                ('ProductAmount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productId', models.IntegerField(primary_key=True, serialize=False)),
                ('productName', models.TextField(max_length=50)),
                ('productType', models.TextField(choices=[('ОВ', 'Овощи'), ('ФП', 'Фрукты'), ('ГП', 'готовая продукция'), ('ПР', 'Прочее')])),
                ('productCost', models.IntegerField()),
                ('productDescription', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('requestId', models.IntegerField(primary_key=True, serialize=False)),
                ('userEmail', models.EmailField(max_length=30)),
                ('requestText', models.TextField()),
            ],
        ),
    ]
