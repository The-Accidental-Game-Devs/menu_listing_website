from django.shortcuts import render

from menu.models import Item


def index_view(request):
    special_items = Item.objects.filter(is_special=True, ).order_by('created_at')[:10]

    return render(request, 'core/index.html', {
        'title': 'Home',
        'special_items': special_items
    })


def learn_more_view(request):
    return render(request, 'core/learn_more.html')
