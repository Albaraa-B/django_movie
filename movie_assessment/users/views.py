from django.shortcuts import render

from django.http import HttpResponse
import requests
import json

from .models import User, User_Fav

# Create your views here.

base_url = 'https://api.themoviedb.org/3'
api_key = 'b105dbabeeabdf41bafb40b2dc0dfea7'

def index(request):
    r = requests.get('{}/movie/latest?api_key={}'.format(base_url, api_key))
    movie = r.json()
    return HttpResponse("Latest Movie: {} -- {}".format(movie['title'], movie['release_date']))

def detail(request, movie_id):
    
    return HttpResponse("You're looking at Movie %s." % movie_id)

def results(request, query):
    response = "You're looking at the results of Search %s."
    return HttpResponse(response % query)

def favorites(request, user_id):
    favs = User_Fav.objects.filter(user_id = user_id)
    name = User.objects.get(pk=user_id)
    return HttpResponse("{} You're voting on Movie {}.".format( name.username, len(favs)))