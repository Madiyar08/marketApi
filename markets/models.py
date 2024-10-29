from django.db import models
from django.utils import timezone


class Market(models.Model):
    MARKET_FORMAT_CHOICES = [
        ('Korzinka', 'Корзинка'),
        ('Korzinka Mahalla', 'Корзинка Махалля'),
        ('Korzinka Diskont', 'Корзинка Дисконт'),
        ('FLO', 'ФЛО'),
        ('REDTAG', 'РЕДТАГ'),
        # Добавь другие форматы, если нужно
    ]

    market_name = models.CharField(max_length=255,blank=True, null=True)
    market_address = models.CharField(max_length=255, blank=True)
    market_orientation = models.CharField(max_length=255, blank=True)
    market_work_time = models.CharField(max_length=150,blank=True, null=True)
    market_phone = models.CharField(max_length=20, blank=True, null=True)
    market_grill = models.CharField(max_length=50, blank=True, null=True)
    manager_full_name = models.CharField(max_length=255, blank=True, null=True)
    manager_phone = models.CharField(max_length=20, blank=True, null=True)
    manager_work_time = models.CharField(max_length=50, blank=True, null=True)
    manager_day_off = models.CharField(max_length=50, blank=True, null=True)
    supervisor_one_full_name = models.CharField(max_length=255, blank=True, null=True)
    supervisor_one_phone = models.CharField(max_length=20, blank=True, null=True)
    supervisor_one_work_time = models.CharField(max_length=50, blank=True, null=True)
    supervisor_one_day_off = models.CharField(max_length=50, blank=True, null=True)
    supervisor_two_full_name = models.CharField(max_length=255, blank=True, null=True)
    supervisor_two_phone = models.CharField(max_length=20, blank=True, null=True)
    supervisor_two_work_time = models.CharField(max_length=50, blank=True, null=True)
    supervisor_two_day_off = models.CharField(max_length=50, blank=True, null=True)
    supervisor_three_full_name = models.CharField(max_length=255, blank=True, null=True)
    supervisor_three_phone = models.CharField(max_length=20, blank=True, null=True)
    supervisor_three_work_time = models.CharField(max_length=50, blank=True, null=True)
    supervisor_three_day_off = models.CharField(max_length=50, blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)

    # Добавляем поле для формата маркета
    market_format = models.CharField(
        max_length=50,
        choices=MARKET_FORMAT_CHOICES,
        default='Korzinka'
    )

    # Поле для даты последнего обновления
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.market_name
