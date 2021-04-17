from django.shortcuts import render
# from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView
import json
# Create your views here.

class Expense(APIView):
     def get(self,request):
         return HttpResponse(json.dumps({'id':123, 'name':'food'}), content_type="application/json; charset=UTF-8")
     
     def post(self, request):
         ...