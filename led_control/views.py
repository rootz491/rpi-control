from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import led
# Create your views here.


def index(request):
        template_name = 'led_control/index.html'
        # print(led.objects.all()[0], ' -> ', led.objects.all()[0].message)
        context = {
                'data': led.objects.all()[0],
        }
        return render(request, template_name, context=context)
        # return HttpResponse('<h1>hello world<h1>')


def update(request):
        if request.method == 'POST':
                current_state = led()
                current_state.is_active = request.POST.__contains__('switch')
                if request.POST['message'] != '':
                        current_state.message = request.POST['message']
                current_state.save()
                # print(request.POST['message'])
                # print(request.POST.__contains__('switch'))
                return HttpResponseRedirect(reverse('led_control:index'))