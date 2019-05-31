from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
import praw, json
from django.http import HttpResponse


ofc = ''

@api_view(['POST','GET'])
def index(request):
    global ofc
    if request.method == 'POST':
     user = request.body
     user = user.decode('utf8').replace("'", '"')
     n = json.loads(user)
     reddit = praw.Reddit(client_id='HTW6y8MNqTcVSw',client_secret='3LIv3N5wfFCgb-f2ldJ11SmdFME',redirect_uri='http://127.0.0.1:8000/auth/', user_agent='testscript by /u/'+n['name'])
     ofc = reddit.auth.url(['identity'], '...', 'permanent')
     return HttpResponse('hello')
    if request.method == 'GET':
      return redirect(ofc)


def start(request):
 return render(request, "build/index.html")

def auth(request):
    return render(request, "build/index.html")    
