from django.shortcuts import render
from .logic.logic_measurements import get_all_measurements
from .logic.logic_measurements import get_measurement
from .logic.logic_measurements import delete_measurement
from django.http import HttpResponse
from django.core import serializers
# Create your views here.

def get_measurements(request):
    measurements = get_all_measurements()
    measurement_list = serializers.serialize('json', measurements)
    return HttpResponse(measurement_list, content_type='application/json')

def get_measurement_id(request, id):
    measurement = get_measurement(id)
    measurement_obj = serializers.serialize('json', measurement)
    return HttpResponse(measurement_obj, content_type='application/json')

def delete_measurement_id(request, id):
    measurement = delete_measurement(id)
    return HttpResponse('Done!!')