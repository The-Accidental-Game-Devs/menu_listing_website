from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from .models import Item
from .forms import NewItemForm, EditItemForm

@login_required
@permission_required('menu.can_create_item')
def new_item_view(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            messages.success(request, "Item created successfully.")
            return redirect(reverse('menu:item_detail', args=[item.pk]))
    else:
        form = NewItemForm()

    return render(request, 'menu/form.html', {
        'title': 'New item',
        'form': form,
        'button_text': 'Create Item',
    })

@login_required
@permission_required('menu.can_edit_item')
def edit_item_view(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, "Item updated successfully.")
            return redirect(reverse('menu:item_detail', args=[item.pk]))

    else:
        form = EditItemForm(instance=item)

    return render(request, 'menu/form.html', {
        'title': 'Edit item',
        'form': form,
        'button_text': 'Edit item',
    })

@login_required
@permission_required('menu.can_delete_item')
def delete_item_view(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if item:
        print(f'Deleting item" {item}')
        messages.success(request, f"Deleted item: {item.name}")
        item.delete()
    else:
        print('Item not found or not owned by the user')

    return redirect('menu:menu')

def menu_view(request):

    items = Item.objects.all()

    return render(request, 'menu/menu.html', {
        'title': 'Menu',
        'items': items,
    })

def detail_view(request, pk):
    item = get_object_or_404(Item, pk=pk)

    return render(request, 'menu/detail.html', {
        'item': item
    })