from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import led
from gpiozero import LED
# Create your views here.

bulb = LED(15)

def index(request):
        template_name = 'led_control/index.html'
        # print(led.objects.all()[0], ' -> ', led.objects.all()[0].message)
        data = led.objects.all()[0]
        changeLedState(data.is_active)
        '''
        if data.is_active:
            bulb.on()
        else:
            bulb.off()
        '''
        context = {
                'data': data,
        }
        return render(request, template_name, context=context)
        # return HttpResponse('<h1>hello world<h1>')


def update(request):
        if request.method == 'POST':
                current_state = led()
                if request.POST.__contains__('switch'):
                    current_state.is_active = True
                if request.POST['message'] != '':
                        current_state.message = request.POST['message']
                current_state.save()
                # print(request.POST['message'])
                # print(request.POST.__contains__('switch'))
                return HttpResponseRedirect(reverse('led_control:index'))
            

def changeLedState(flag):
    print(flag, ' is here')
    if flag:
        bulb.on()
        return 'LED on'
    else:
        bulb.off()
        return 'LED off'
