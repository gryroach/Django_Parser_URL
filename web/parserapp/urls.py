from django.urls import path
from .views import temp_list, DomainView

urlpatterns = [
    path("parser/", temp_list),
    path("", DomainView.as_view())
]
