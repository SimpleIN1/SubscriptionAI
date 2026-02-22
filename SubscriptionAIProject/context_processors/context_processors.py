from django.conf import settings


def website_data(request):
    return {
        "SITE_DOMAIN": settings.SITE_DOMAIN,
        "SITE_NAME": settings.SITE_NAME,
    }


def metrics(request):
    return {
        "METRIC_URL": settings.METRIC_URL,
        "METRIC_SITE_ID": settings.METRIC_SITE_ID
    }
