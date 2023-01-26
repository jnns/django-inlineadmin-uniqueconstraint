from django.contrib import admin

from example.models import Pizza, PizzaTopping, Topping


class PizzaToppingInline(admin.TabularInline):
    model = PizzaTopping


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    inlines = [PizzaToppingInline]
    exclude = ["toppings"]


admin.site.register(Topping)
