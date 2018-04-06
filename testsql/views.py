from django.shortcuts import render
from .models import SUser
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from . import dao
from django.contrib import messages
#from .forms import  Resisterform,redirect

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
        #아이디와 비밀번호가 맞을 경우, userMain이라는 페이지 이동(개인별 디비 접속 조회 가능)
        if userid==val["id"] and userpw==val["pw"]:
             return render(request,"userMain.html",{
                 "userid" : userid,
                 "userpw" : userpw,
             })
        #아이디와 비밀번호가 맞지 않을경우
        else:             
             return HttpResponseRedirect('/')
             
@csrf_exempt
def registuser(request):
    return render(request,"registuser.html")
  

@csrf_exempt
def registercheck(request):
    suserid = request.POST.get('ruserid')
    alluser = dao.bringalluser()
    #전체 유저중 아이디만 검색하여 id가 중복되는지를 검사하는 과정
    for val in alluser:
        #아이디는 중복 할 수 없기때문에 아이디가 겹치면 무조건 /register로...
        if suserid==val["id"]:
            return HttpResponseRedirect('/register')
        else:
            pass
            #현재 아이디중 입력값과 동일한게 없다면? ->받아온다.
            #공백,최대문자길이 html 단에서 처리....
            
           # return HttpResponseRedirect('/')




#informtion자료 보여주는 곳
def Informations(request):
    pass

#스케쥴 관리 보여주는 view
def Schedules(request):
    pass
 #   return render(request,"Information.html")


            

    
            
  

    
