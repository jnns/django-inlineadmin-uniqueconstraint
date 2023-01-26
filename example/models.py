from django.db import models


class Pizza(models.Model):
    toppings = models.ManyToManyField(to="Topping")


class Topping(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PizzaTopping(models.Model):
    pizza = models.ForeignKey("Pizza", on_delete=models.CASCADE)
    topping = models.ForeignKey("Topping", on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint("pizza", "topping", name="unique_pizza_topping")
        ]
