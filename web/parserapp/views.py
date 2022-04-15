from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from rest_framework.parsers import JSONParser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_swagger.views import get_swagger_view
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from .serializers import DomainSerializer
from .models import DomainModel
from .tasks import background_finding_data_from_remote_api
from .src.filters import DomainFilter


validator = URLValidator()


@api_view(['GET', 'POST'])
def parser_view(request):

    if request.method == 'GET':
        return Response("Please, send URL by POST-request", status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            url = data['url']
        except Exception as er:
            return Response({"success": False, "message": str(er)}, status=status.HTTP_400_BAD_REQUEST)
        try:
            validator(url)
        except ValidationError as val_er:
            return Response({"success": False, "message": val_er}, status=status.HTTP_400_BAD_REQUEST)
        background_finding_data_from_remote_api.delay(url)
        return Response({"success": True, "message": "Data sent"}, status=status.HTTP_201_CREATED)


class DomainView(ListAPIView):
    queryset = DomainModel.objects.all()
    serializer_class = DomainSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = DomainFilter
    ordering_fields = ['url', 'domain', 'country', 'create_date', 'update_date', 'isDead']


schema_view = get_swagger_view(title='Domains API')
