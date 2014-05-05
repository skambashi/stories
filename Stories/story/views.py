from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # TODO: Add boostrap to landing page (need to be able to serve static media and make base html page)
    return HttpResponse("Story says Hello World!")