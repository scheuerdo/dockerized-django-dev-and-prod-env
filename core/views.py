from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm


def create_item(request):
    """Create a new item."""
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_items")
    else:
        form = ItemForm()
    return render(request, "core/create_item.html", {"form": form})


def list_items(request):
    """List all items from the Item model."""
    items = Item.objects.all()
    return render(request, "core/list_items.html", {"items": items})


def update_item(request, pk):
    """Update an item."""
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("list_items")
    else:
        form = ItemForm(instance=item)
    return render(request, "core/update_item.html", {"form": form})


def delete_item(request, pk):
    """Delete an item."""
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return redirect("list_items")


# Privacy Policy, Impressum, About and Contact Views for the sake of completeness
def privacy_policy(request):
    return render(request, "core/privacy_policy.html")


def impressum(request):
    return render(request, "core/impressum.html")


def about(request):
    return render(request, "core/about.html")


def contact(request):
    return render(request, "core/contact.html")
