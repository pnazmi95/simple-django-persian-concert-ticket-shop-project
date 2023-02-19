from django.db import models
from django.contrib.auth.models import User


class ProfileModel(models.Model):
    class Meta:
        verbose_name = "حساب کاربری"
        verbose_name_plural = "حساب های کاربری"

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="کاربر", related_name="profile")

    profile_pic = models.ImageField(
        upload_to="profile_images/", null=True, blank=True, verbose_name="تصویر کاربر")

    male = 1
    female = 2
    choices = (
        (male, "مرد"),
        (female, "زن")
    )
    gender = models.IntegerField(
        choices=choices, null=True, blank=True, verbose_name="جنسیت")

    credit = models.IntegerField(verbose_name="اعتبار", default=0)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
