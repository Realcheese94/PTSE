from django.db import models

#사회복지사 
class SUser(models.Model):
    SuserId = models.CharField(max_length=10,null=False)
    Suserpw = models.CharField(max_length=10,null=False)
    Susername = models.CharField(max_length=10,null=False)
    Susertel = models.CharField(max_length=11,null=False)
    Suserimage =models.ImageField(default='default.png',blank=True)
    def __str__(self):
        return self.SuserId
        
#독거 노인 테이블 , 독거노인 이름, 담당 복지사이름        
class NUser(models.Model):
    NUsername =models.CharField(max_length=10,null=False)
    Chargeuser = models.ForeignKey(SUser, on_delete=models.CASCADE, null = True)

#사회복지사 일정 테이블
class UserCalendar(models.Model):
    Userid = models.ForeignKey(SUser, on_delete=models.CASCADE,null =True)
    Uyear = models.IntegerField(null =True)
    Udate = models.IntegerField(null = True)
    Udoing = models.CharField(max_length=20, null=True)

#사회복지사 Todolist , 자신이 업무를 하면서 까먹거나 잊지 않게 메모장 형식, 체크박스로 삭제가능.
class UserTodo(models.Model):
    Todoname = models.CharField(max_length=20,null=True)
    TodoUserno = models.CharField(max_length=10,null = True)
# Create your models here.
