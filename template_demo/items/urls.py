from django.urls import path
from .views import item_list  # import your view function

urlpatterns = [
    path('', item_list, name='item_list'),  # root of this app
]
