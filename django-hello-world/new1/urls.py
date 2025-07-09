from django.urls import path
from new1.views import index

urlpatterns = [
    path('hello', index, name='hello')
]