# Generated by Django 4.1.2 on 2022-10-27 19:10

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
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_images/', verbose_name='تصویر کاربر')),
                ('gender', models.IntegerField(blank=True, choices=[('male', 'مرد'), ('female', 'زن')], null=True, verbose_name='جنسیت')),
                ('credit', models.IntegerField(default=0, verbose_name='اعتبار')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'حساب کاربری',
                'verbose_name_plural': 'حساب های کاربری',
            },
        ),
    ]
