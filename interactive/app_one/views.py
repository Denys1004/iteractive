from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
from datetime import datetime
from django.core.paginator import Paginator

from django.forms.models import model_to_dict # Need for sortation

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    context = {
        'posts': Post.objects.all().order_by('-created_at'),
        'videos': Video_item.objects.all()
    }
    return render(request, 'video.html', context)



# REGISTRATION
def create_user(request):
    if request.method == "GET":
        return render(request, "register.html")
    else:
        request.session.clear()
        request.session['first_name'] = request.POST['first_name']
        request.session['last_name'] = request.POST['last_name']
        request.session['birth_date'] = request.POST['birth_date']
        request.session['email'] = request.POST['email']
        errors = User.objects.validator(request.POST)	
        if len(errors)>0:													
            for value in errors.values():											
                messages.error(request, value)											
            return redirect('/register')
        new_user = User.objects.register(request.POST)
        request.session.clear()
        request.session['user_id'] = new_user.id
        first_i = new_user.first_name[0]
        last_i = new_user.last_name[0]
        initials = first_i + last_i
        request.session['initials'] = initials
        return redirect('/dashboard')

# LOGIN
def login(request):
    if request.method == "GET":
        if 'user_id' in request.session:
            request.session.clear()
            return render(request, "login.html")
        else:
            return render(request, "login.html")
    else:
        result = User.objects.authenticate(request.POST['email'],request.POST['password']) # Checking login
        if result == False:
            messages.error(request, "Email or passwort do not match.")
            return redirect('/login')
        else:
            user = User.objects.get(email = request.POST['email'])
            request.session['user_id'] = user.id
            first_i = user.first_name[0]
            last_i = user.last_name[0]
            initials = first_i + last_i
            request.session['initials'] = initials
            return redirect('/dashboard')
        


# CREATE NEW POST
def create_new_post(request):
    if request.method == "GET":
        context = {
            'videos': Video_item.objects.all(),
            'cur_user': User.objects.get(id = request.session['user_id']),
        }
        return redirect('/dashboard')

    else:
        poster = User.objects.get(id = request.session['user_id'])
        this_post = Post.objects.create(title = request.POST['title'], content = request.POST['content'],poster = poster)
        this_video = Video_item.objects.create(video = request.POST['video_item'], video_poster = poster, post = this_post)
        messages.success(request, "Post Successfully Created!")
        return redirect('/dashboard')

