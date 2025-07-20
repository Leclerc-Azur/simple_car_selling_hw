from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Car(models.Model):
    title = models.CharField("Название", max_length=100)
    model = models.CharField("Модель", max_length=100)
    year = models.PositiveSmallIntegerField("Год выпуска")
    image = models.ImageField("Изображение", upload_to='images/')
    price = models.DecimalField("Цена", max_digits=12, decimal_places=2)
    description = models.TextField("Описание", max_length=800)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.PROTECT)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
