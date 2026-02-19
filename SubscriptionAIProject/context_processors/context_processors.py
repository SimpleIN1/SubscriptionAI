from django.conf import settings


def website_data(request):
    return {
        "SITE_DOMAIN": settings.SITE_DOMAIN,
        "SITE_NAME": settings.SITE_NAME,
    }
