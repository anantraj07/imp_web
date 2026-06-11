from django.shortcuts import render
from .models import SiteConfig

def index(request):
    config = SiteConfig.objects.first()
    if not config:
        config = SiteConfig.objects.create()
    return render(request, "welcome/index.html", {"config": config})
    
def guide(request):
    config = SiteConfig.objects.first()
    if not config:
        config = SiteConfig.objects.create()
    return render(request, "welcome/guide.html", {"config": config})
