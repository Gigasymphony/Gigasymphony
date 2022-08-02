import locale  # import DAY_1
from django.shortcuts import render


# Create your views here.
def home(request):
    import json
    import requests
    days_in_week = [0, 1, 2, 3, 4, 5, 6]
    weeks_weather = []

    api_requests = requests.get(
        "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Doncaster?unitGroup=metric&include=days&key=NHRJSZ2JMDZHYT8BWKHFYWFRZ&contentType=json")

    try:
        api = json.loads(api_requests.content)

    except Exception:
        api = "Error"

    
        
            


     

    return render(request, 'home.html', {'api': api, 'week': days_in_week, 'weeks_weather': weeks_weather})


def about(request):
    return render(request, 'about.html', {})
