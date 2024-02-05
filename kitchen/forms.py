from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from kitchen.models import Cook, Dish


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "username",
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
        )


class CookUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
        )


class DishCreationForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(queryset=get_user_model().objects.all(),
                                          widget=forms.CheckboxSelectMultiple,)

    class Meta:
        model = Dish
        fields = ["name", "description", "price", "dish_type", "cooks"]


class DishUpdateForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(queryset=get_user_model().objects.all(),
                                          widget=forms.CheckboxSelectMultiple,)

    class Meta:
        model = Dish
        fields = ["name", "description", "price", "dish_type", "cooks"]


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by dish name"
            }
        )

    )