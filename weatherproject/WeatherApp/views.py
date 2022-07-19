from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def home(request):  
    if request.method=='POST':
        city = request.POST.get('city', 'True')
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=imperial&appid=f877d78a3ad76be6e0726a58c6821e12').read()
        list_of_data = json.loads(source)  #convert content into python dict
        context = {'city':city,"country_code": str(list_of_data['sys']['country']),"coordinate": str(list_of_data['coord']['lon']) + ' '+ str(list_of_data['coord']['lat']), "temp": str(list_of_data['main']['temp']) + 'k', "pressure": str(list_of_data['main']['pressure']),"humidity": str(list_of_data['main']['humidity'])}  
    else:  
        context={}  
      
    # send dictionary to the index.html  
    return render(request, 'index.html', context)  