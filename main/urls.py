from django.urls import path

from . import views


urlpatterns = [
   # path ("", views.index, name="index"),
   # path ("v1/", views.v1, name="view1"),
    path("<int:id>", views.index, name="index"),
    path("", views.home, name = "home")
]