from django.urls import path
from .views import HomeView, UserUpdateView, UserDeleteView


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("update/<int:pk>/", UserUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", UserDeleteView.as_view(), name="delete"),
]
