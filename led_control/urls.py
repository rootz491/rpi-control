from django.urls import path
from .views import *

app_name = 'led_control'

urlpatterns = [
        path('', index, name='index'),
        path('update', update, name='update'),
]