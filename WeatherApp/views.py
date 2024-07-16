from django.shortcuts import render
import requests

# Create your views here.
def index(request):

    appid = '7c2e049482a114ec7cfa4bbcf5ee1c7f'
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': 'Los Angeles', 'appid':appid, 'units':'metric'}

    r = requests.get(url=URL, params=PARAMS)
    data = r.json()

    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp = data['main']['temp']

    return render(request, 'index.html', {'description': description, 'icon': icon, 'temp': temp})