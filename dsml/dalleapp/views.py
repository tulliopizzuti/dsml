from django.shortcuts import render
from .models import Text
# Create your views here.

def index(req):
    return render(req,'index.html')

def texts(req):
    return render(req,'texts.html')

def wordtree(req):
    return render(req,'wordtree.html')
