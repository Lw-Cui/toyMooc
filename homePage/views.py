# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth, messages
from models import UserProfile, Course
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    dict = {}
    if request.user.is_authenticated():
        dict["login"] = True
        dict["username"] = request.user.username
        user = UserProfile.objects.get(user=request.user)
        dict["courses"] = Course.objects.exclude(user=user)
    else:
        dict["login"] = False
        dict["courses"] = Course.objects.all()
    return render_to_response("profile.html", dict)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect("/")
        else:
            messages.info(request, 'Username or password error.')
    return render_to_response("login.html", RequestContext(request))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def regist(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        confirm = request.POST.get('confirm', '')
        if password == confirm:
            user = User()
            user.username = username
            user.set_password(password)
            user.save()
            UserProfile.objects.create(user=user)
            newuser = auth.authenticate(username=username, password=password)
            auth.login(request, newuser)
            return HttpResponseRedirect("/")
        else:
            messages.info(request, 'confirm password isn\'t equal to password')
    return render_to_response("regist.html", RequestContext(request))

def course(request):
    dict = {}
    if request.user.is_authenticated():
        user = UserProfile.objects.get(user=request.user)
        dict["courses"] = Course.objects.exclude(user=user)
        dict["login"] = True
        dict["username"] = request.user.username
    else:
        dict["courses"] = Course.objects.all()
    return render_to_response("course.html", dict)

@csrf_exempt
def add_course(request):
    sheet = {}
    if request.user.is_authenticated():
        try:
            user = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            user = UserProfile.objects.create(user=request.user)
        choose = Course.objects.get(title=request.POST.get('title', ''))
        choose.user.add(user)
        sheet["name"] = request.POST.get('title', '')
    return HttpResponse(json.dumps(sheet))

@csrf_exempt
def cancel_course(request):
    sheet = {}
    if request.user.is_authenticated():
        user = UserProfile.objects.get(user=request.user)
        title = request.POST.get('title', '')
        choose = Course.objects.get(title=title)
        choose.user.remove(user)
        sheet["name"] = title
    return HttpResponse(json.dumps(sheet))

def manage(request):
    dict = {}
    if request.user.is_authenticated():
        try:
            user = UserProfile.objects.get(user=request.user)
        except:
            user = UserProfile.objects.create(user=request.user)
        dict["courses"] = user.course_set.all()
        dict["login"] = True
    return render_to_response('manage.html', dict)
