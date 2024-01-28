from django import forms
from django.contrib.auth.forms import UserCreationForm

from kitchen.models import Cook, Dish


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
        )


class DishCreationForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ["name", "description", "price", "dish_type", "cooks"]