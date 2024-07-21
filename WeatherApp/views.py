from django.shortcuts import render
import requests
import datetime
from decouple import config

# Create your views here.
def index(request):

    if 'city' in request.POST and request.POST['city']:
        city = request.POST['city']
    else:
        city = 'Los Angeles'

    appid = config('API_KEY')
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': city, 'appid':appid, 'units':'metric'}

    r = requests.get(url=URL, params=PARAMS)
    data = r.json()

    context = {
        'description': data['weather'][0]['description'].title,
        'icon': data['weather'][0]['icon'],
        'temp': (int(data['main']['temp'] * 2)) + 30,
        'humidity': data['main']['humidity'],
        'city': city.title,
        'day': datetime.date.today()
     }
    return render(request, 'index.html', context)