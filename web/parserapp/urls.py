from django.urls import path
from .views import temp_list

urlpatterns = [
    path("", temp_list),
]
