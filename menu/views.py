from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q

from .models import Item, Category
from .forms import NewItemForm, EditItemForm, CategoryForm


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

    return render(request, 'menu/form.html', {'title': 'New item', 'form': form, 'button_text': 'Create Item', })


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

    return render(request, 'menu/form.html', {'title': 'Edit item', 'form': form, 'button_text': 'Update item', })


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
        messages.error(request, f"Failed to delete item: {item.name}")

    return redirect('menu:menu')


def menu_view(request):
    search_query = request.GET.get('search', '')
    category_filter = request.GET.get('category', None)

    try:
        category_filter = int(category_filter)
    except (ValueError, TypeError):
        category_filter = None

    items = Item.objects.all()
    categories = Category.objects.all()

    if search_query:
        items = items.filter(Q(name__icontains=search_query) | Q(detail__icontains=search_query))

    if category_filter:
        items = items.filter(category_id=category_filter)

    return render(request, 'menu/menu.html',
                  {'title': 'Menu', 'items': items, 'search_query': search_query, 'categories': categories,
                   'category_filter': category_filter, })


def detail_view(request, pk):
    item = get_object_or_404(Item, pk=pk)

    return render(request, 'menu/detail.html', {'item': item})


@login_required
@permission_required('menu.can_create_category')
def new_category_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)

        if form.is_valid():
            category = form.save(commit=False)
            category.created_by = request.user
            category.save()
            messages.success(request, "Category created successfully.")
            return redirect('menu:menu')
    else:
        form = CategoryForm()

    return render(request, 'menu/form.html',
                  {'title': 'New category', 'form': form, 'button_text': 'Create category', })


@login_required
@permission_required('menu.can_edit_category')
def edit_category_view(request, pk):
    category = get_object_or_404(Category, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)

        if form.is_valid():
            form.save()
            messages.success(request, "Category updated successfully.")
            return redirect('menu:menu')

    else:
        form = CategoryForm(instance=category)

    return render(request, 'menu/form.html',
                  {'title': 'Edit category', 'form': form, 'button_text': 'Update category', })


@login_required
@permission_required('menu.can_delete_item')
def delete_category_view(request, pk):
    category = get_object_or_404(Category, pk=pk, created_by=request.user)

    if category:
        print(f'Deleting item" {category}')
        messages.success(request, f"Deleted category: {category.name}")
        category.delete()
    else:
        print('Category not found or not owned by the user')
        messages.error(request, f"Failed to delete category: {category.name}")

    return redirect('menu:menu')


@login_required
@permission_required('menu.can_view_category')
def category_view(request):
    categories = Category.objects.all()

    return render(request, 'menu/category.html', {'title': 'Category', 'categories': categories, })
