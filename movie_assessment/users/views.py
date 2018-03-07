from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

import requests
import json

from .models import User, User_Fav

# Create your views here.

base_url = 'https://api.themoviedb.org/3'
api_key = 'b105dbabeeabdf41bafb40b2dc0dfea7'

def index(request):
    r = requests.get('{}/movie/latest?api_key={}'.format(base_url, api_key))
    movie = r.json()
    
    template = loader.get_template('users/index.html')
    context = {
        'latest': movie,
    }
    return HttpResponse(template.render(context, request))
    

def detail(request, movie_id):
    r = requests.get('{}/movie/{}?api_key={}'.format(base_url, movie_id, api_key))
    if r.status_code == 200:
        movie = r.json()
        template = loader.get_template('users/detail.html')
        context = {
            'movie': movie,
        }
        return HttpResponse(template.render(context, request))
    elif r.status_code == 404:
        return HttpResponse('Not Found')
    else:
        return HttpResponse('API Issues')

def results(request, query):
    response = "You're looking at the results of Search %s."
    return HttpResponse(response % query)

def favorites(request, user_id):
    favs = User_Fav.objects.filter(user_id = user_id)
    name = User.objects.get(pk=user_id)
    return HttpResponse("{} You're voting on Movie {}.".format( name.username, len(favs)))