# Generated by Django 4.1.2 on 2022-10-28 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timemodel',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'فروش بلیط شروع شده است'), (2, 'فروش بلیط تمام شده است'), (3, 'این سانس کنسل شده است'), (4, 'در حال فروش بلیط')], null=True, verbose_name='وضعیت'),
        ),
    ]
