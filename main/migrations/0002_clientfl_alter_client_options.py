# Generated by Django 4.1.7 on 2023-03-23 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientFL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIO', models.CharField(max_length=250, verbose_name='ФИО')),
                ('client_code', models.CharField(max_length=250, verbose_name='код клиента')),
                ('passport_data', models.CharField(max_length=250, verbose_name='Паспортные данные')),
                ('Date_of_birth', models.CharField(max_length=250, verbose_name='Дата рождения')),
                ('address', models.CharField(max_length=250, verbose_name='Адрес')),
                ('mail', models.CharField(max_length=250, verbose_name='e-mail')),
                ('password', models.CharField(max_length=250, verbose_name='пароль')),
            ],
            options={
                'verbose_name': 'Клиент ФЛ',
                'verbose_name_plural': 'Клиенты ФЛ',
            },
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Клиент ЮЛ', 'verbose_name_plural': 'Клиенты ЮЛ'},
        ),
    ]