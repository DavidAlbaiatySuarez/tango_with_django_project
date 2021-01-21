from django.shortcuts import render
from django.http import HttpResponse
'''
Each view exists withing views.py as a series of individual functions
We have now created one view called index.
Each view takes at least one argument (an HttpRequest - convention to call
it request) and return one HttpResponse (what we want to send to the client
requesting the view.
'''
def index(request):
    return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About</a>")

def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")
