from django.shortcuts import render
from django.http import HttpResponse
import requests
import json




base_url = 'https://api.themoviedb.org/3'
api_key = 'b105dbabeeabdf41bafb40b2dc0dfea7'




# Create your views here.
def index(request):
    r = requests.get('{}/movie/latest?api_key={}'.format(base_url, api_key))
    movie = r.json()
    return HttpResponse("Latest Movie: {} -- {}".format(movie['title'], movie['release_date']))