from django.conf import settings


def website_data(request):
    return {
        "DOMAIN_SITE": settings.DOMAIN_SITE
    }
