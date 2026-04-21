from django.db import models

class User(models.Model):
    FIO = models.CharField(max_length=100)
    namber = models.IntegerField()

    def __str__(self):
        return self.FIO

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    attribute_2 = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

class Performer(models.Model):
    description = models.CharField(max_length=200)
    FIO = models.CharField(max_length=100)
    name = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return self.FIO

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

class Order(models.Model):
    quantity = models.IntegerField()
    Performer = models.ForeignKey(Performer, on_delete=models.CASCADE)
    Service = models.ForeignKey(Service, on_delete=models.PROTECT)
    User = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"Заказ #{self.id} - {self.User.FIO}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'