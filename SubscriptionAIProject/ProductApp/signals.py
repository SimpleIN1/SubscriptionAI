
from django.conf import settings
from django.core.cache import cache
from django.dispatch import receiver
from ProductApp.models import ProductModel
from django.db.models.signals import post_save, post_delete


@receiver(post_save, sender=ProductModel)
@receiver(post_delete, sender=ProductModel)
def clear_cache(sender, instance, **kwargs):
    cache.delete(settings.CACHE_PRODUCTS_KEY)
