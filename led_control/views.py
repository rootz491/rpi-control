from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
        template_name = 'led_control/index.html'
        return render(request, template_name)
        # return HttpResponse('<h1>hello world<h1>')