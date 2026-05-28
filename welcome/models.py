from django.db import models

class SiteConfig(models.Model):
    batch_year = models.CharField(max_length=10, default="2025", help_text="e.g. 2025")
    gform_url = models.URLField(
        max_length=500,
        default="https://forms.google.com",
        help_text="Google Form URL for newcomers to fill"
    )
    whatsapp_channel_url = models.URLField(
        max_length=500,
        blank=True,
        default="",
        help_text="WhatsApp Channel invite link"
    )
    announcement = models.TextField(
        blank=True,
        default="",
        help_text="Optional announcement banner (leave blank to hide)"
    )
    admission_date = models.CharField(
        max_length=50,
        default="16th July",
        help_text="Admission date to display"
    )

    class Meta:
        verbose_name = "Site Configuration"
        verbose_name_plural = "Site Configuration"

    def __str__(self):
        return f"Config — Batch {self.batch_year}"
