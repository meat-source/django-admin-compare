from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=50)
    age = models.SmallIntegerField()
    color = models.CharField(max_length=50)

    objects = models.Manager()  # явно указываем, чтобы использовать подсказки

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return self.name
