from django.urls import path
from .views import parser_view, DomainView, schema_view

urlpatterns = [
    path("parser/", parser_view),
    path("", DomainView.as_view()),
    path("docs/", schema_view)
]
