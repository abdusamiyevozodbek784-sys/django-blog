from django.db import models


class User(models.Model):
    telegram_id = models.BigIntegerField(unique=True, null=True, verbose_name='Foydalanuvchi Telegram ID')
    username = models.CharField(max_length=50, null=True, verbose_name='Foydalanuvchi Username')
    user_full_name = models.CharField(max_length=25, null=True, verbose_name='Foydalanuvchi ism familiyasi')
    phone_number = models.CharField(max_length=18, blank=True, verbose_name='Foydalanuvchi raqami')
    language = models.CharField(max_length=10, blank=True, null=True, verbose_name='Telegram Tili')

    def __str__(self):
        return f"{self.telegram_id} | {self.user_full_name}"

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'


class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True, verbose_name='Kategoriya nomi')


    def __str__(self):
        return f"{self.category_name}"


    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
