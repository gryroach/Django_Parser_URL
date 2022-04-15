from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import DomainSerializer
from .models import DomainModel
from .tasks import background_finding_data_from_remote_api
from .src.filters import DomainFilter


@api_view(['GET'])
def parser_view(request):

    if request.method == 'GET':
        try:
            url = request.GET.get('url', None)
            background_finding_data_from_remote_api.delay(url)
        except Exception as er:
            return Response({"success": False, "message": str(er)})
        return Response("Data sent", status=200)


class DomainView(ListAPIView):
    queryset = DomainModel.objects.all()
    serializer_class = DomainSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = DomainFilter
    ordering_fields = ['url', 'domain', 'country', 'create_date', 'update_date', 'isDead']
