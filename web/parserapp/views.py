from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .serializers import DomainSerializer
from .models import DomainModel
from .src.get_data import create_records_db


@api_view(['GET'])
def parser_view(request):

    if request.method == 'GET':
        try:
            url = request.GET.get('url', None)
        except Exception as er:
            return Response({"success": False, "message": str(er)})
        return Response(create_records_db(url))


class DomainView(ListAPIView):
    serializer_class = DomainSerializer
    queryset = DomainModel.objects.all()
