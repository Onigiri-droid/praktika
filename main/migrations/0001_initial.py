# Generated by Django 4.1.7 on 2023-03-23 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=250, verbose_name='Название компании')),
                ('address', models.CharField(max_length=250, verbose_name='Адрес')),
                ('INN', models.CharField(max_length=250, verbose_name='ИНН')),
                ('r_score', models.CharField(max_length=250, verbose_name='р/с')),
                ('BIC', models.CharField(max_length=250, verbose_name='БИК')),
                ('name_manager', models.CharField(max_length=250, verbose_name='ФИО')),
                ('contact_person', models.CharField(max_length=250, verbose_name='ФИО контактного лица')),
                ('tel_contact_person', models.CharField(max_length=250, verbose_name='телефон контактного лица')),
                ('mail', models.CharField(max_length=250, verbose_name='e-mail')),
                ('password', models.CharField(max_length=250, verbose_name='пароль')),
                ('client_code', models.CharField(max_length=250, verbose_name='код клиента')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_employee', models.CharField(max_length=250, verbose_name='Код сотрудника')),
                ('post', models.CharField(max_length=250, verbose_name='Должность')),
                ('FIO', models.CharField(max_length=250, verbose_name='ФИО')),
                ('login', models.CharField(max_length=250, verbose_name='Логин')),
                ('password', models.CharField(max_length=250, verbose_name='пароль')),
                ('orders', models.CharField(blank=True, max_length=250, verbose_name='Заказы')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(blank=True, max_length=250, verbose_name='ID')),
                ('order_number', models.CharField(max_length=250, verbose_name='Номер заказа')),
                ('date_creation', models.CharField(max_length=250, verbose_name='Дата создания')),
                ('client_code', models.CharField(max_length=250, verbose_name='Код клиента')),
                ('article', models.CharField(max_length=250, verbose_name='Артиикул')),
                ('status', models.CharField(max_length=250, verbose_name='Статус')),
                ('closing_date', models.CharField(blank=True, max_length=250, verbose_name='Дата закрытия')),
                ('employee_code', models.CharField(max_length=250, verbose_name='Код сотрудника')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(blank=True, max_length=250, verbose_name='ID')),
                ('product', models.CharField(max_length=250, verbose_name='Наименование товара')),
                ('art', models.CharField(max_length=250, verbose_name='Артикул')),
                ('price', models.CharField(max_length=250, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
