from django.db import models
from accounts.models import ProfileModel
from jalali_date import datetime2jalali


class ConcertModel(models.Model):
    class Meta:
        verbose_name = "کنسرت"
        verbose_name_plural = "کنسرت ها"

    name = models.CharField(max_length=100, null=True,
                            blank=True, verbose_name="نام کنسرت")
    singer_name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="نام خواننده")
    length = models.IntegerField(
        null=True, blank=True, verbose_name="مدت زمان کنسرت")
    poster = models.ImageField(
        upload_to="concert_images/", null=True, blank=True, verbose_name="پوستر")

    def __str__(self):
        return self.singer_name


class LocationModel(models.Model):
    class Meta:
        verbose_name = "مکان برگزاری کنسرت"
        verbose_name_plural = "مکان های برگزاری کنسرت"

    name = models.CharField(max_length=100, null=True,
                            blank=True, verbose_name="نام محل برگزاری")
    address = models.CharField(
        max_length=500, null=True, blank=True, verbose_name="آدرس محل برگزاری")
    phone_number = models.CharField(
        max_length=11, null=True, blank=True, verbose_name="شماره تلفن محل برگزاری")
    capacity = models.IntegerField(
        null=True, blank=True, verbose_name="ظرفیت محل برگزاری")

    def __str__(self):
        return self.name


class TimeModel(models.Model):
    class Meta:
        verbose_name = "سانس"
        verbose_name_plural = "سانس ها"

    concert = models.ForeignKey(
        "ConcertModel", on_delete=models.PROTECT, verbose_name="نام کنسرت")
    location = models.ForeignKey(
        "LocationModel", on_delete=models.PROTECT, verbose_name="محل برگزاری کنسرت")
    start_date_time = models.DateTimeField(
        null=True, blank=True, verbose_name="زمان شروع کنسرت")
    seats = models.IntegerField(
        null=True, blank=True, verbose_name="تعداد صندلی")

    start = 1
    end = 2
    canceled = 3
    on_sale = 4

    status_choices = (
        (start, "فروش بلیط شروع شده است"),
        (end, "فروش بلیط تمام شده است"),
        (canceled, "این سانس کنسل شده است"),
        (on_sale, "در حال فروش بلیط"),
    )

    status = models.IntegerField(
        choices=status_choices, null=True, blank=True, verbose_name="وضعیت")

    def __str__(self):
        return f"Time: {self.start_date_time}, concert name: {self.concert.name}, location: {self.location.name}"

    def get_jalali_date_time(self):
        return datetime2jalali(self.start_date_time)


class TicketModel(models.Model):
    class Meta:
        verbose_name = "بلیط"
        verbose_name_plural = "بلیط ها"

    profile = models.ForeignKey(
        ProfileModel, on_delete=models.PROTECT, verbose_name="نام کاربر مرتبط")
    time = models.ForeignKey(
        "TimeModel", on_delete=models.PROTECT, verbose_name="سانس")
    name = models.CharField(max_length=100, null=True,
                            blank=True, verbose_name="عنوان")
    price = models.IntegerField(null=True, blank=True, verbose_name="قیمت")
    ticket_img = models.ImageField(
        upload_to="ticket_images/", null=True, blank=True, verbose_name="عکس")

    def __str__(self):
        return f"TicketInfo: Profile: {self.profile.__str__()} ConcertInfo: {self.time.__str__()}"
