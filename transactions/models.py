from django.db import models
from django.utils import timezone
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        # Приводим имя категории к нижнему регистру перед сохранением
        self.name = self.name.lower()
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)  # Позволяем null и blank

    def save(self, *args, **kwargs):
        if not self.date:
            self.date = timezone.now()  # Устанавливаем текущую дату и время, если дата не указана
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.amount} - {self.category.name if self.category else 'No Category'} - {self.date}"
