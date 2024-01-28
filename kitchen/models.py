from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(default=0)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "cooker"
        verbose_name_plural = "cookers"

    def __str__(self):
        return (f"{self.first_name} "
                f"{self.last_name} "
                f"({self.years_of_experience} years of experience)")


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook, related_name="dishes")

    class Meta:
        ordering = ["dish_type", "name", "price"]

    def __str__(self):
        return (f"{self.name} (Price: {self.price}) "
                f"cooked by: {', '.join(cook.get_full_name() for cook in self.cooks.all())}")
