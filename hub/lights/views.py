from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from lights.models import Light
import json

def index(request):
	#lightList = ''
	#for light in Light.objects.all(): 
	#	lightList+=(str(light.id) + ' | ' + light.description + '<br>')
	lightsDict = dict(lights=list(Light.objects.values('id', 'description')))
	return JsonResponse(lightsDict)

def detail(request, light_id):
	try:
		light = Light.objects.get(pk=light_id)
		return HttpResponse(str(light.id) + ' | ' + light.description)

	except Light.DoesNotExist:
		return HttpResponseNotFound(-1)

def toggle(request, light_id):
	light = Light.objects.get(pk=light_id)
	response = HttpResponse(light.toggle())

	#response['Access-Control-Allow-Origin'] = "*"
	#response['Access-Control-Allow-Methods'] = "POST, OPTIONS"
	#response['Access-Control-Allow-Headers'] = "X-Requested-With"
	#response['Access-Control-Max-Age'] = "1800"
		
	return response

     
        
