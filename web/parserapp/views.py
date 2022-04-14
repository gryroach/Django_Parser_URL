from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from .src.parsers import ParserLinks
from .serializers import DomainSerializer
from .models import DomainModel
import logging


@api_view(['GET'])
def temp_list(request):

    if request.method == 'GET':
        url = request.GET['url']
        logging.warning(url)
        result = ParserLinks(url).find_links()
        return Response(str(result))


class DomainView(ListCreateAPIView):
    serializer_class = DomainSerializer
    queryset = DomainModel.objects.all()
