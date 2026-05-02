# 🔐 Django Modular Authentication (Class 22)

A modular Django project featuring a reusable `accounts` app. This system handles user registration, secure login/logout, and page protection using decorators.

---

## ✅ Project Checklist

- [x] **App Creation:** Created a standalone `accounts` app for authentication.
- [x] **Logic:** Implemented `register`, `login`, and `logout` functions in `views.py`.
- [x] **Protection:** Applied `@login_required` to restrict access to the Dashboard and Contact pages.
- [x] **Integration:** Successfully exported the `accounts` app to the `static_pages` project.
- [x] **Security:** Included `{% csrf_token %}` in all forms to prevent CSRF attacks.

---

## 💻 Core Implementation

### 1. `accounts/views.py` 
```python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def landing(request):
    return render(request, 'landing.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password != password2:
            messages.error(request, 'Passwords do not match.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Account created. Please log in.')
            return redirect('login')
    return render(request, 'register.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def event(request):
    return render(request, 'event.html')




def logout_view(request):
    logout(request)
    return redirect('landing')
```

### 2. `config/settings.py`
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
]

LOGIN_URL = 'login'
```

### 3. `accounts/urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('event/', views.event, name='event'),
    path('logout/', views.logout_view, name='logout'),
]
```

---

## 🔗 Project Links
- **Repository:** https://github.com/lazy-h-null/my-exercise-archive/tree/main/22-apr16
  
```