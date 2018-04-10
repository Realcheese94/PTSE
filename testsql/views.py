from django.shortcuts import render
from .models import SUser
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
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

            context = {'userid':userid,
                       'userpw':userpw,
                       'username':val["name"],
                       'userno':val["no"],
                       'usertel':val["tel"],
                       }

            request.session['context']= context

            return render(request,"Main.html")
        #아이디와 비밀번호가 맞지 않을경우
        else:             
             return HttpResponseRedirect('/')
             
  
#회원가입 유효성 검증 def
@csrf_exempt
def registercheck(request):
    ruserid = request.POST.get('ruserid')
    ruserpw = request.POST.get('ruserpw')
    rusername = request.POST.get('rusername')
    rusertel = request.POST.get('rusertel')
    ruserinfo = request.POST.get('ruserinfo')    
    alluser = dao.bringalluserid()
    #전체 유저중 아이디만 검색하여 id가 중복되는지를 검사하는 과정
    for val in alluser:
        #아이디는 중복 할 수 없기때문에 아이디가 겹치면 무조건 /register로...
        if val==ruserid:
            return render(request,"registuser.html")
        else:
            #dic ={'id':row[1],'pw':row[2]}
            rf = SUser(SuserId=ruserid,Suserpw=ruserpw,Susername=rusername,Susertel=rusertel)
            rf.save()
            return HttpResponseRedirect('/')
            #현재 아이디중 입력값과 동일한게 없다면? ->받아온다.
            #공백,최대문자길이 html 단에서 처리.... 
            

           # return HttpResponseRedirect('/')

#regist창으로 가는 def
def registuser(request):
    return render(request,"registuser.html")
    


#informtion자료 보여주는 곳
def Informations(request):
    
    if request.session.:
        userid = request.session["context"]['userid']
        username = request.session["context"]['username']
        usertel = request.session["context"]['usertel']
        userno = request.session["context"]['userno']
        return render(request, "information.html",{"userid" : userid,
                                               "username": username,
                                               "usertel": usertel,
                                               "userno":userno
    })
    else:
        return render(request,"information.html")

#스케쥴 관리 보여주는 view
def Schedules(request):
    return render(request,"Schedule.html")
 #   return render(request,"Information.html")


            

    
            
  

    
