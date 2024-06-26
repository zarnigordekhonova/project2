# Generated by Django 5.0.4 on 2024-04-30 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='available_tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=255)),
                ('number_econom_tickets', models.IntegerField()),
                ('number_business_tickets', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tickets_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_ticket1', models.CharField(max_length=255)),
                ('price_ticket1', models.IntegerField()),
                ('type_ticket2', models.CharField(max_length=255)),
                ('price_ticket2', models.IntegerField()),
            ],
        ),
    ]
