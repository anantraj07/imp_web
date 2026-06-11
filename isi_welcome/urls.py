from django.contrib import admin
from django.urls import path, include
from django.conf import settings

admin.site.site_header = "ISI Welcome — Admin"
admin.site.site_title = "ISI GR Admin"
admin.site.index_title = "Manage Site Configuration"

urlpatterns = [
    path(settings.ADMIN_PATH, admin.site.urls),
    path("", include("welcome.urls")),
    path("", views.index, name="index"),
    path("guide/", views.guide, name="guide"),
]


