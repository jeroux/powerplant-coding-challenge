from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema

from django.http import HttpResponse, JsonResponse

from .serializers import PayloadSerializer, ResultSerializer

@extend_schema(
        request=PayloadSerializer,
        responses={201: ResultSerializer},
        methods=["POST"]
    )
@api_view(['POST'])
def calculThePower(request):
    """
    Take the JSON in the request and return the powerplant list
    """
    # Get the JSON from the request
    payload = PayloadSerializer(data=request.data)

    if payload.is_valid():
        print(payload.data)
        return JsonResponse(payload.data, status=201)
    # Get the load
    #print(payload.data)
    # Get the fuels
    # Get the powerplants


    # Calculate the powerplant list
    # Return the powerplant list
    return JsonResponse(payload.errors, status=400)
