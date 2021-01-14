from django.http import HttpResponse 
from datetime import datetime
from django.http import JsonResponse
from django.http import QueryDict

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh hi, the current time is {now}'.format(now=str(now)))

def hi(request):
    #mapea los valores que llegan el objeto request
    numbers = map(int, request.GET['numbers'].split(','))
    print(numbers)
    #ordena los valores 
    numbers = sorted(numbers)
    print(numbers)
    #crea un diccionario
    numbers = {'numbers': numbers}
    print(type(numbers))
    #crea el objeto de tipo Jsonresponse
    response = JsonResponse(numbers, json_dumps_params={'indent': 4})
    return HttpResponse(response)