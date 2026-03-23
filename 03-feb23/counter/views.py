from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

counter_value = 0

def index(request):
    """Render the main counter page"""
    global counter_value
    return render(request, 'counter/index.html', {'counter': counter_value})

def increment(request):
    """Increment counter and return new value"""
    global counter_value
    counter_value += 1
    return HttpResponse(str(counter_value))

def decrement(request):
    """Decrement counter and return new value"""
    global counter_value
    counter_value -= 1
    return HttpResponse(str(counter_value))

def reset(request):
    """Reset counter to zero"""
    global counter_value
    counter_value = 0
    return HttpResponse(str(counter_value))