from django.http import HttpResponse, HttpResponseNotFound
from lights.models import Light

def index(request):
	lightList = ''
	for light in Light.objects.all(): 
		lightList+=(str(light.id) + ' | ' + light.description + '<br>')
	return HttpResponse(lightList)

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

     
        
