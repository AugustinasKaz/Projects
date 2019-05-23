from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Calculator, Comment
from .serializers import Love_serializer, Love_serializer_comment
from django.shortcuts import render
from django.http import HttpResponse

import requests, json

@api_view(['POST'])  
def get_names(request):
  post_data = request.body
  post_data = post_data.decode('utf8').replace("'", '"')
  n = json.loads(post_data)
  response = requests.get("https://love-calculator.p.rapidapi.com/getPercentage?fname="+n['name1']+"&sname="+n['name2'],
  headers={"X-RapidAPI-Host": "love-calculator.p.rapidapi.com", "X-RapidAPI-Key": "7b059f2d74msh3df7699123c451fp186ba5jsn5d233eed0fb8"})
  r = response.json()
  error = False
  try:
     p = Calculator(first_name = r['fname'],second_name = r['sname'],percentage = r['percentage'],result = r['result'])
     p.save()
     Cal_id = p.id
  except KeyError:
     p = Calculator(message = r['message'])
     error = True
     p.save()
     Cal_id = p.id
  res_data = {'err':error, 'ids':Cal_id}  
  return HttpResponse(json.dumps(res_data))

@api_view(['POST'])  
def get_comment(request):
   post_data2 = request.body
   post_data2 = post_data2.decode('utf8').replace("'", '"')
   data = json.loads(post_data2)
   print(data['user'], data['comment'])
   p = Comment(author = data['user'], text = data['comment'])
   p.save()
   return HttpResponse("s")
    


@api_view(['GET'])
def get_results(request):
     calculator = Calculator.objects.all()
     serializer = Love_serializer(calculator, many=True)
     return Response({"response": serializer.data})
  
@api_view(['GET'])
def all_comments(request):
   comments = Comment.objects.all()
   serializer = Love_serializer_comment(comments, many=True)
   return Response({"response": serializer.data})    



def index(request):
 return render(request, "build/index.html")        











 