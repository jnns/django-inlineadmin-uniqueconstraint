from example.models import Topping


def test_inline_admin_unique_constraint_validation(client, admin_user):
    client.force_login(admin_user)
    rocket = Topping.objects.create(name="Rocket")
    response = client.post(
        "/admin/example/pizza/add/",
        data={
            "pizzatopping_set-TOTAL_FORMS": "2",
            "pizzatopping_set-INITIAL_FORMS": "0",
            "pizzatopping_set-MIN_NUM_FORMS": "0",
            "pizzatopping_set-MAX_NUM_FORMS": "1000",
            "pizzatopping_set-0-id": "",
            "pizzatopping_set-0-pizza": "",
            "pizzatopping_set-0-topping": rocket.pk,
            "pizzatopping_set-1-id": "",
            "pizzatopping_set-1-pizza": "",
            "pizzatopping_set-1-topping": rocket.pk,
        },
    )
