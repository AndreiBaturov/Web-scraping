#1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json; написать функцию, возвращающую список репозиториев.

import json
import os
#from pprint import pprint

import requests
from dotenv import load_dotenv

# относительный путь для примера, лучше использовать глобальный!
#load_dotenv("/mnt/c/Users/Andrei_Baturov.MOSCOW/Documents/Course/creds/.env")
load_dotenv("./creds/.env")

owner = os.getenv("CLIENT_ID")
token = os.getenv("GITHUB_TOKEN")
path = 'repos.json'

def get_list_of_repos(owner, token, path):
    query_url = f"https://api.github.com/users/{owner}/repos"

    #pprint(owner)
    #pprint(token)

    headers = {'Authorization': f'token {token}'}
    params = {
        "sort": "full_name"
    }
    r = requests.get(query_url, headers=headers, params=params)

    with open(path, 'w') as json_file:
      json.dump(r.json(), json_file)

get_list_of_repos(owner, token, path)


#2. Зарегистрироваться на https://openweathermap.org/api и написать функцию, которая получает погоду в данный момент для города,
# название которого получается через input. https://openweathermap.org/current

import json
from pprint import pprint
import requests

city = input(f"Введите город:\n")
country_code = input(f"Введите сокращенный код страны:\n")
APIkey = input(f"Введите APIkey:\n")

def get_weather_by_city(city, country_code, apikey):
    query_url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={APIkey}"

    headers = {'Authorization': f'token {APIkey}'}
    params = {
        "units": "metric"
    }
    r = requests.get(query_url, headers=headers, params=params)

    pprint(r.json())

get_weather_by_city(city, country_code, APIkey)