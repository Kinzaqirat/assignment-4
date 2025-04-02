import requests

api_key='82a9c2c582df86ca8863d184e0ca5bf7'
user_input=input("Enter city: ")
weather_data=requests.get(
    # f'http://api.openweathermap.org/data/2.5/forecast?q={user_input}&appid={api_key}'
    # f'http://api.openweathermap.org/data/2.5/forecast?id={user_input}&appid={api_key}'
 
   f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}&units=metric"

)
weather =weather_data.json()['weather'][0]['main']
tem=weather_data.json()["main"]['temp']
if weather_data.json()['cod']=="404":
    print('No city found')
else:
    print(f"The weather in {user_input} is {weather}")
    print(f"The Tempeature in {user_input} is {tem}")


