from django.urls import path
from .views import parser_view, DomainView

urlpatterns = [
    path("parser/", parser_view),
    path("", DomainView.as_view())
]
