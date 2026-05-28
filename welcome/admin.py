from django.contrib import admin
from .models import SiteConfig

@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    list_display = ("batch_year", "admission_date", "gform_url")

    def has_add_permission(self, request):
        # Only one config row allowed
        return not SiteConfig.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
