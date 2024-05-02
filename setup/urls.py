from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("loginJwt/", include("loginJwt.urls")),
    path("admin/", admin.site.urls),
]