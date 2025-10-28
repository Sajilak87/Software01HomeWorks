import requests


city_name = input("Enter municipality name: ")
app_key = 'd17ec7d9893a877ceee5548bd52dae9a'

request = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={app_key}&units=metric"

try:
    response = requests.get(request)
    if response.status_code==200:
        json_response = response.json()
        desc= str(json_response['weather'][0]['description'])
        print( "Weather: ",desc)
        print("Temperature: " , str(json_response['main']['temp']) + "Celsius")
except requests.exceptions.RequestException as e:
    print ("Request could not be completed.")