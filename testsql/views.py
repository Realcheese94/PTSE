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
        #아이디와 비밀번호가 맞을 경우, userMain이라는 페이지 생성
        if userid==val["id"] and userpw==val["pw"]:
             return render(request,"userMain.html",{
                 "userid" : userid,
                 "userpw" : userpw
             })
        #아이디와 비밀번호가 맞지 않을경우
        else:
             
             return render(request,"Main.html")

def registuser(request):
    pass