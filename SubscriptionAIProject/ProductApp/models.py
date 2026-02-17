import os

import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator


def upload_to(instance, filename) -> str:
    """
    фукнция корректирорвки имени файла
    :param instance:
    :param filename:
    :return:
    """
    path = "products"
    _, extension = os.path.splitext(filename)
    return f"{path}/{uuid.uuid4()}{extension}"


class ProductModel(models.Model):
    BADGE_CHOICES = (
        (1, "Пусто"),
        (2, "Лучший выбор"),
        (3, "Безлимит"),
        (4, "Новинка"),
        (5, "Хит"),
    )
    TERM_CHOICES = (
        (1, "1 МЕСЯЦ"),
        (2, "2 МЕСЯЦА"),
        (3, "3 МЕСЯЦА"),
        (4, "4 МЕСЯЦА"),
        (5, "5 МЕСЯЦЕВ"),
        (6, "6 МЕСЯЦЕВ"),
        (7, "1 ГОД"),
        (8, "2 ГОДА"),
        (9, "3 ГОДА"),
    )

    uuid = models.UUIDField(default=uuid.uuid4)
    badge = models.PositiveSmallIntegerField(choices=BADGE_CHOICES, default=1)
    card_featured = models.BooleanField(default=False)
    title = models.CharField(max_length=250)
    term = models.PositiveSmallIntegerField(choices=TERM_CHOICES, default=1)
    subtitle = models.CharField(max_length=250)
    price = models.FloatField(
        validators=[MinValueValidator(0.00)],
        default=0.00)
    features_html = models.TextField(null=True, blank=True)
    description_html = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_to)

    def title_replace_br(self):
        return self.title.replace('<br/>', ' ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
