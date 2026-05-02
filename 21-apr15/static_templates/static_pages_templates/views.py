from django.shortcuts import render

# Create your views here.

def home(request):
    ctx = {
        'name': "Tony",
        'age': 25,
        'gains': 2344.322211,
        'skills': ['Python', 'Django', 'Tailwind', 'SQLite', 'Docker', 'Git'],
        'info': {
            'Location': 'Seoul',
            'Role': 'Developer',
            'Status': 'Active',
            'Project': 'Static Site',
            'Engine': 'Django 5.0'
        }
    }
    return render(request, 'static_pages_templates/home.html', ctx)

def contact(request):
    return render(request, 'static_pages_templates/contact.html')

def faq(request):
    return render(request, 'static_pages_templates/faq.html')

def about(request):
    return render(request, 'static_pages_templates/about.html')