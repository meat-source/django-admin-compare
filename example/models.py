from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=50)
    age = models.SmallIntegerField()
    color = models.CharField(max_length=50)

    objects = models.Manager()  # явно указываем, чтобы использовать подсказки

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def __str__(self):
        return self.name
