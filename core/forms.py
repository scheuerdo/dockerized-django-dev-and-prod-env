from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    """
    Form class for Item model.
    Allows the User to create or edit a new item to the database.
    """

    class Meta:
        model = Item
        fields = ["name", "price"]
