from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("hello, world. you're at the polls index. 안녕~")



# "~~" 요안의 리스펀스를 xlient에게 전달해준다.
