from django.contrib import admin
from ProductApp import models


@admin.action(description="Change status from inactive to active")
def change_status_active(modeladmin, request, queryset):
    queryset.update(active=True)


@admin.action(description="Change status from active to inactive")
def change_status_inactive(modeladmin, request, queryset):
    queryset.update(active=False)


@admin.register(models.ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("title_replace_br", "price", "active", "term", "badge", )
    list_filter = ("term", )

    search_fields = ("title", )

    actions = [
        change_status_active,
        change_status_inactive,
    ]
