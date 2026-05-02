from django.shortcuts import render

# Create your views here.

def home(request):
    ctx = {
        'name': "Tony",
        'age': 25,
        'gains': 2344.322211
    }
    return render(request, 'static_pages_templates/home.html', ctx)

def contact(request):
    return render(request, 'static_pages_templates/contact.html')

def faq(request):
    return render(request, 'static_pages_templates/faq.html')

def about(request):
    return render(request, 'static_pages_templates/about.html')