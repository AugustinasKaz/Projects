from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
import praw, json, requests
import requests.auth
from django.http import HttpResponse

class User:
  def __init__(self, name, reddit, redirect_url):
    self.name = name
    self.reddit = reddit
    self.redirect_url = redirect_url

p1 = User('','','')

@api_view(['POST','GET'])
def index(request):
    if request.method == 'POST':
      user = request.body
      user = user.decode('utf8').replace("'", '"')
      n = json.loads(user)
      reddit = praw.Reddit(client_id='HTW6y8MNqTcVSw',client_secret='3LIv3N5wfFCgb-f2ldJ11SmdFME',redirect_uri='http://127.0.0.1:8000/auth/', user_agent='testscript by /u/'+n['name'])
      p1.name = n['name']
      p1.reddit = reddit
      p1.redirect_url = reddit.auth.url(['identity'], '...', 'permanent')
      return HttpResponse('hello')
    if request.method == 'GET':
      return redirect(p1.redirect_url)




def start(request):
 return render(request, "build/index.html")

def auth(request):  
  return render(request, "build/index.html")   

@api_view(['GET', 'POST'])
def UserData(request):
  sub_type = request.body
  sub_type = sub_type.decode('utf8').replace("'", '"')
  sub_type = json.loads(sub_type)
  reddit = p1.reddit
  dict = {}
  lst = []
  for submission in reddit.subreddit(sub_type['sort']).hot(limit=10):
    dict = {'title': submission.title, 'url': submission.url, 'upvotes': submission.score, 'subreddit': str(submission.subreddit), 'author': str(submission.author)}
    lst.append(dict)

  return HttpResponse(json.dumps(lst))
