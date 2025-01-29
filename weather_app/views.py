from django.shortcuts import render
import requests

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        api_key = 'ac97b4a45bf9f7f94d8d960d16fc3a36'  
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        
        try:
            response = requests.get(url)
            weather_data = response.json()
            
            context = {
                'city': city,
                'temperature': round(weather_data['main']['temp']),
                'description': weather_data['weather'][0]['description'],
                'icon': weather_data['weather'][0]['icon'],
                'humidity': weather_data['main']['humidity'],
                'wind_speed': weather_data['wind']['speed'],
            }
        except:
            context = {
                'error': 'City not found. Please try again.'
            }
        
        return render(request, 'weather_app/index.html', context)
    
    return render(request, 'weather_app/index.html')