# inventory/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from inventory.models import Item, Category
from .forms import ItemForm


def home(request):
    return render(request, 'inventory/home.html')

def contact(request):
    return render(request, 'inventory/contact.html')

@login_required
def add_category(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            Category.objects.get_or_create(user=request.user, name=name)
        return redirect("category_list")
    return render(request, "inventory/add_category.html")

@login_required
def category_list(request):
    categorys = Category.objects.filter(user=request.user)
    return render(request, 'inventory/category_list.html', {'categorys': categorys})

@login_required
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id, user=request.user)
    
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    
    return render(request, 'inventory/confirm_category_delete.html', {'category': category})

@login_required
def items_list(request):
    items = Item.objects.filter(user=request.user)
    return render(request, 'inventory/items_list.html', {'items': items})

@login_required
def item_details(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'inventory/item_details.html', {'item': item})

@login_required
def add_item(request):
    if request.method == "POST":
        print(request.FILES)
        form = ItemForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('items_list')
    else:
        form = ItemForm(user=request.user)

    return render(request, "inventory/add_item.html", {"form": form})


@login_required
def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_details', item_id=item.id)
    else:
        form = ItemForm(instance=item)
    
    return render(request, 'inventory/edit_item.html', {'form': form, 'item': item})

@login_required
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('items_list')
