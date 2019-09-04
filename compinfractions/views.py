from django.shortcuts import render
from pathlib import Path

import json, os
import urllib.parse as urlparse

# Create your views here.
def index(req):
    with open( os.path.dirname(os.path.realpath(__file__)) + '\infractions.json', 'r') as fp:
        data = json.loads(fp.read())

        data.sort(key=lambda s: s['infractions_speed'])
        
        return render(req, 'compinfractions/index.html', {'infractions': data}) 

def search(req, infractions_speed):
    with open( os.path.dirname(os.path.realpath(__file__)) + '\infractions.json', 'r') as fp:
        data = json.loads(fp.read())

        data.sort(key=lambda s: s['infractions_speed'])


        gevonden = []
        for d in data:
            if d['infractions_speed'] >= infractions_speed:
                gevonden.append(d)
        print(gevonden)
        return render(req, 'compinfractions/search.html', {'infractions': gevonden})