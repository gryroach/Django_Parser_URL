from rest_framework.decorators import api_view
from rest_framework.response import Response
from .src.parsers import ParserLinks
import logging


@api_view(['GET'])
def temp_list(request):

    if request.method == 'GET':
        url = request.GET['url']
        logging.warning(url)
        result = ParserLinks(url).find_links()
        return Response(str(result))
