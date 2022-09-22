import json
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    #request --> HttpRequest --> Django
    # if request.method != "POST":
    #     return Response({"Detail": "GET not allowed"}, status=405) #If not using DRF
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
    #     data = model_to_dict(instance, fields=['id', 'title', 'price'])
    return Response(data)
    #     json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers={"content-type": "application/json"})


@api_view(["POST"])
def api_post(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"Invalid": "Not good data"}, status=400)


