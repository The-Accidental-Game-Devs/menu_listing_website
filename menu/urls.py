from django.urls import path
from .views import new_item_view, edit_item_view, delete_item_view, menu_view, detail_view, new_category_view, \
    edit_category_view, delete_category_view, category_view

app_name = 'menu'

urlpatterns = [
    path('item/new/', new_item_view, name='new_item'),
    path('item/<int:pk>/edit/', edit_item_view, name='edit_item'),
    path('item/<int:pk>/delete/', delete_item_view, name='delete_item'),
    path('', menu_view, name='menu'),
    path('item/<int:pk>/', detail_view, name='item_detail'),
    path('category/new/', new_category_view, name='new_category'),
    path('category/<int:pk>/edit/', edit_category_view, name='edit_category'),
    path('category/<int:pk>/delete/', delete_category_view, name='delete_category'),
    path('category/', category_view, name='category'),
]
