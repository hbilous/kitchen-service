from django.contrib.auth import get_user_model
from django.test import TestCase
from kitchen.models import DishType, Dish


class ModelsTests(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="test")
        self.assertEqual(str(dish_type), dish_type.name)

    def test_cook_str(self):
        cook = get_user_model().objects.create(
            username="tester",
            first_name="test1",
            last_name="test2",
            password="Test12345",
            years_of_experience=3
        )
        self.assertEqual(str(cook), f"{cook.first_name} "
                                    f"{cook.last_name} "
                                    f"({cook.years_of_experience} years of experience)")

    def test_dish_str(self):
        cook = get_user_model().objects.create_user(
            username="tester",
            first_name="test1",
            last_name="test2",
            password="Test12345",
            years_of_experience=3
        )
        dish_type = DishType.objects.create(name="test")
        dish = Dish.objects.create(
            name="Fish",
            description="test description",
            price=10.25,
            dish_type=dish_type
        )
        dish.cooks.set([cook])
        expected_str = f"{dish.name} (Price: {dish.price}) cooked by: {cook.get_full_name()}"
        self.assertEqual(str(dish), expected_str)
