from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UrlSerializer

@api_view(['POST'])
def make_url_short(request):

    data  = request.data

    url_serializer = UrlSerializer(data=data)
    if url_serializer.is_valid():
        return Response("Working")


    

