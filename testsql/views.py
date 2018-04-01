from django.shortcuts import render
from .models import SUser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import dao
from django.contrib import messages

# Create your views here.
def index(request):
    SUserlist = SUser.objects.all()
    return render(request,'Main.html')

@csrf_exempt
def loginuser(request):
    values=""
    alluser = dao.bringalluser()
    userid = request.POST.get('UserID')
    userpw = request.POST.get('UserPW')
    for val in alluser:
        if userid==val["id"] and userpw==val["pw"]:
             return render(request,"userMain.html",{
                 "userid" : userid,
                 "userpw" : userpw
             })
        else:
             messages.warning(request, 'Please check your ID/PW')
             return render(request,"Main.html")

def registuser(request):
    pass