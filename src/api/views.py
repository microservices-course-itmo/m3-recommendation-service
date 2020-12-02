from django.shortcuts import render
import json
from rest_framework import views, status
from rest_framework.response import Response
from ml.registry import MLRegistry
from recommendations.wsgi import registry

class PredictView(views.APIView):
    def post(self, request, endpoint_name, format=None):
        algorithm_object = registry.endpoints[endpoint_name]
        prediction = algorithm_object.predict(request.data)

        return Response(prediction)