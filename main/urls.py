from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path ("", views.index, name="index"),
    #path ("v1/", views.v1, name="view1"),
    path("<int:id>", views.index, name="index"),
    path("", views.home, name = "home"),
    path("home/", views.home, name = "home"),
    path("create/", views.cadastro, name = "cadastro"),#formulario de cadastro
    path("2/", views.cadastro, name = "list"),
    path("upload/", views.subir, name = "upload"),
    path("portifolio/", views.portifolio, name = "portifolio"),
] 

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

