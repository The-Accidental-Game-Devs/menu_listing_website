from django.urls import path

from .views import index_view, learn_more_view

app_name = 'core'

urlpatterns = [
    path('', index_view, name='home'),
    path('learn-more/', learn_more_view, name='learn_more'),
]
