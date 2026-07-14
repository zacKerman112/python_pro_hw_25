from django.contrib import admin
from django.urls import URLPattern, path

from counter.views import index


urlpatterns: list[URLPattern] = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
]
