from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from control.models import Light, FanSpeed, Toggler
import json

def index(request):
	controlDict = dict(controls=list(Toggler.objects.all().values('id','description')))
	return JsonResponse(controlDict)

def lights(request):
	try:
		lightsDict = dict(lights=list(Light.objects.all().values('id','description')))
		return JsonResponse(lightsDict)
	except Light.DoesNotExist:
		return HttpResponseNotFound(-1)

def fanspeeds(request):
        try:
                fanspDict = dict(fanspeeds=list(FanSpeed.objects.all().values('id','description')))
                return JsonResponse(fanspDict)
        except FanSpeed.DoesNotExist:
                return HttpResponseNotFound(-1)

def detail(request, toggler_id):
	try:
		controlDict = dict(control=list(Toggler.objects.filter(pk=toggler_id).values('id','description')))
		return JsonResponse(controlDict)
	except Toggler.DoesNotExist:
		return HttpResponseNotFound(-1)

def toggle(request, toggler_id):
	control = Toggler.objects.get(pk=toggler_id)
	response = HttpResponse(control.toggle())

	#response['Access-Control-Allow-Origin'] = "*"
	#response['Access-Control-Allow-Methods'] = "POST, OPTIONS"
	#response['Access-Control-Allow-Headers'] = "X-Requested-With"
	#response['Access-Control-Max-Age'] = "1800"
		
	return response

     
        
