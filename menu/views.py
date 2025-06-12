from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.decorators.http import require_POST

from .forms import NewItemForm, EditItemForm, CategoryForm
from .models import Item, Category


@staff_member_required
@permission_required('menu.add_item', raise_exception=True)
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


@staff_member_required
@permission_required('menu.change_item', raise_exception=True)
def edit_item_view(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            if form.has_changed():
                changed_fields = form.changed_data  # List of changed field names
                instance = form.save(commit=False)
                instance.save(update_fields=changed_fields)
                form.save_m2m()
                messages.success(request, "Item updated successfully.")
            else:
                messages.info(request, "No changes detected.")
            return redirect(reverse('menu:item_detail', args=[item.pk]))

    else:
        form = EditItemForm(instance=item)

    return render(request, 'menu/form.html', {'title': 'Edit item', 'form': form, 'button_text': 'Update item', })


def delete_item_object(pk, user) -> str:
    item = get_object_or_404(Item, pk=pk)

    if not user.has_perm('menu.delete_item'):
        raise PermissionDenied

    item_name = item.name
    item.delete()
    return item_name


@require_POST
@staff_member_required
def delete_item_view(request, pk):
    if request.headers.get('x-requested-with') != 'XMLHttpRequest':
        return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)

    try:
        name = delete_item_object(pk, request.user)
        return JsonResponse({'success': True, 'message': f'Deleted item: {name}'}, status=200)
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=400)


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

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('menu/partials/item_list.html', {'items': items}, request=request)
        return JsonResponse({'html': html})

    return render(request, 'menu/menu.html', {'title': 'Menu', 'search_query': search_query, 'categories': categories,
                                              'category_filter': category_filter, })


def detail_view(request, pk):
    item = get_object_or_404(Item, pk=pk)

    return render(request, 'menu/detail.html', {'item': item})


@staff_member_required
@permission_required('menu.add_category', raise_exception=True)
def new_category_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)

        if form.is_valid():
            category = form.save(commit=False)
            category.created_by = request.user
            category.save()
            messages.success(request, "Category created successfully.")
            return redirect(reverse('menu:category'))
    else:
        form = CategoryForm()

    return render(request, 'menu/form.html',
                  {'title': 'New category', 'form': form, 'button_text': 'Create category', })


@staff_member_required
@permission_required('menu.change_category', raise_exception=True)
def edit_category_view(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)

        if form.is_valid():
            if form.has_changed():
                changed_fields = form.changed_data
                instance = form.save(commit=False)
                instance.save(update_fields=changed_fields)
                form.save_m2m()
                messages.success(request, "Category updated successfully.")
            else:
                messages.info(request, "No changes detected.")
            return redirect(reverse('menu:category'))

    else:
        form = CategoryForm(instance=category)

    return render(request, 'menu/form.html',
                  {'title': 'Edit category', 'form': form, 'button_text': 'Update category', })


def delete_category_object(pk, user) -> str:
    category = get_object_or_404(Category, pk=pk)

    if not user.has_perm('menu.delete_category'):
        raise PermissionDenied

    category_name = category.name
    category.delete()
    return category_name


@require_POST
@staff_member_required
def delete_category_view(request, pk):
    if request.headers.get('x-requested-with') != 'XMLHttpRequest':
        return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)

    try:
        name = delete_category_object(pk, request.user)
        return JsonResponse({'success': True, 'message': f'Deleted category: {name}'}, status=200)
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=400)


def category_view(request):
    search_query = request.GET.get('search', '')
    categories = Category.objects.all()
    if search_query:
        categories = categories.filter(Q(name__icontains=search_query))

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('menu/partials/category_list.html', {'categories': categories}, request=request)
        return JsonResponse({'html': html})

    return render(request, 'menu/category.html', {'title': 'Category', 'search_query': search_query, })
