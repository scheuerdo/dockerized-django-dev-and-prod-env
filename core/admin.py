from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """
    Admin class for Item model.
    Shows name and price of the item in the admin panel.
    """

    list_display = ("name", "price")
