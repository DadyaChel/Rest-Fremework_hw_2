import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

from .models import *
from rest_framework import generics
from .serialisers import *
from rest_framework import viewsets


@csrf_exempt
def create_positions(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_tweet = Positions.objects.create(**data)
        json_data = {
            'position': new_tweet.position,
            'department': new_tweet.department
        }
        return JsonResponse(json_data, safe=False)
    if request.method == 'GET':
        tweets = Positions.objects.all()
        data = []
        for tweet in tweets:
            data.append(
                {
                    'position': tweet.position,
                    'department': tweet.department
                }
            )
        json_data = json.dumps(data)
        return JsonResponse(json_data, safe=False)


@csrf_exempt
def create_employee(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_tweet = Employee.objects.create(**data)
        json_data = {
            'FIO': new_tweet.FIO,
            'date_birth': new_tweet.date_birth,
            'position': new_tweet.position.id,
            'zp': new_tweet.zp
        }
        return JsonResponse(json_data, safe=False)
    if request.method == 'GET':
        tweets = Employee.objects.all()
        data = []
        for tweet in tweets:
            data.append(
                {
                    'FIO': tweet.FIO,
                    'date_birth': str(tweet.date_birth),
                    'position': tweet.position.id,
                    'zp': tweet.zp
                }
            )
            print(data)
            print(type(tweet.date_birth))
        json_data = json.dumps(data)
        return JsonResponse(json_data, safe=False)

