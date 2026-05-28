from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "ISI Welcome — Admin"
admin.site.site_title = "ISI GR Admin"
admin.site.index_title = "Manage Site Configuration"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("welcome.urls")),
]
