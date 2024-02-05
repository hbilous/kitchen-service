from django.urls import path

from .views import index, CookListView, DishTypeListView, DishListView, DishTypeCreateView, DishTypeDeleteView, \
    DishTypeUpdateView, DishTypeDetailView, CookCreateView, CookUpdateView, CookDeleteView, DishDetailView, \
    DishCreateView, DishUpdateView, DishDeleteView, CookDetailView

urlpatterns = [
    path("", index, name="index"),
    path("cookers/", CookListView.as_view(), name="cook-list"),
    path("cookers/create/", CookCreateView.as_view(), name="cook-create"),
    path("cookers/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cookers/<int:pk>/update/", CookUpdateView.as_view(), name="cook-update"),
    path("cookers/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish-types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dish-types/<int:pk>/", DishTypeDetailView.as_view(), name="dish-type-detail"),
    path("dish-types/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("dish-types/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish-type-delete"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
]

app_name = "kitchen"
