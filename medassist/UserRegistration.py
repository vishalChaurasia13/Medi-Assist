from django.shortcuts import render,redirect
from . import Pool
import random
import json
import requests

from datetime import date
import time
from django.http import JsonResponse

def UserRegistrationInterface(request):
    return render(request, "UserRegistration.html", {'msg': ''})
def UserLogin(request):
    return render(request, "LoginPage.html", {'msg': ''})

def CheckEmailIdAndPasswd(request):
        email=request.POST['email']
        password = request.POST['password']
        db, cmd = Pool.ConnectionPooling()

        q = "Select * from userregistration where useremail='{}' and userpassword='{}'".format(email,password)
        cmd.execute(q)
        data = cmd.fetchone()
        if (data):
             request.session['user'] = [data['username'],data['usernum'],data['useremail']]
             return WomacForm(request)
        else:
             return render(request, "LoginPage.html", {'msg': 'Invalid EmailId/Password'})





def OtpPage(request):
    btn=request.POST['btn']
    if(btn=="Login"):
        db, cmd = Pool.ConnectionPooling()
        mobileno = request.POST['mobileno']
        q = "Select * from userregistration where usernum='{}'".format(mobileno)
        cmd.execute(q)
        data = cmd.fetchone()
        if (data):
           otp=random.randint(1000,9999)
           print(otp,data)
           mob=mobileno.split("-")
           url="xxxxxxxx{}{}".format(mob[1],otp)
           result=requests.get(url)
           print(url,result)

           request.session['user']=  request.session['user'] = [data['username'],data['usernum'],data['useremail']]
           return render(request, "OTPverification.html", {'otp':otp})
        else:
           return render(request, "LoginPage.html", {'msg': 'Invalid Mobile Number'})

    else:
      return render(request, "UserRegistration.html", {'msg': ''})

def ChkOtp(request):
    d1=request.POST['digit1']
    d2 = request.POST['digit2']
    d3 = request.POST['digit3']
    d4 = request.POST['digit4']
    gotp = request.POST['gotp']
    iotp=d1+d2+d3+d4
    print("test",iotp,gotp)
    if(gotp==iotp):

        return WomacForm(request)
    else:
        return render(request, "OTPverification.html", {"msg":"Invalid Otp"})



def UserRegistrationDisplayAll(request):
    try:
        db, cmd = Pool.ConnectionPooling()
        q = "Select * From userregistration"
        cmd.execute(q)
        records = cmd.fetchall()
        db.close()
        return render(request, "DisplayAllUserRegistration.html", {'result': records})
    except Exception as e:
        print(e)
        return render(request, "DisplayAllUserRegistration.html", {'result': {}})


def UserRegistrationSubmit(request):
    try:
        db, cmd = Pool.ConnectionPooling()
        username = request.POST['username']
        usercity = request.POST['usercity']
        useremail = request.POST['useremail']
        userdob = request.POST['userdob']
        tor = request.POST['tor']
        usernum = request.POST['usernum']
        userpassword = request.POST['userpassword']

        q = "insert into userregistration(username,usercity, useremail, userdob, tor,usernum,userpassword) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(username, usercity, useremail, userdob, tor,usernum,userpassword)
        print(q)
        cmd.execute(q)
        db.commit()
        db.close()
        return render(request, "UserRegistration.html", {'msg': 'Record Submitted'})
    except Exception as e:
        print(e)
        return render(request, "UserRegistration.html", {'msg': 'Fail To Submit Record'})
def UserLoginInterface(request):
    return render(request, "UserLoginInterface.html", {'msg': ""})

def EmailLogin(request):
    return render(request, "EmailLogin.html")

def ForgetPassword(request):
    return render(request, "ForgetPassword.html", {'msg': ""})


def WomacForm(request):
    try:
        db,cmd= Pool.ConnectionPooling()
        q="Select * from doctorregistration"
        cmd.execute(q)
        data=cmd.fetchall()

        return render(request, "WomacSurveys.html", {'msg': "",'Data':data,'UserName':request.session['user'][0]})
    except Exception as e:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(e)
        return render(request, "WomacSurveys.html", {'msg': ""})

def SurveyInterface(request):
    try:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        sid=request.POST['sid']
        db, cmd = Pool.ConnectionPooling()
        q = "Select * from doctorregistration where doctorid='{0}'".format(sid)
        cmd.execute(q)
        doctor = cmd.fetchall()
        print(doctor)
        request.session['doctor']=doctor[0]['doctorid']

        q = "Select * from specialization where specializationid='{0}'".format(doctor[0]['specialization'])
        cmd.execute(q)
        spl = cmd.fetchall()
        print(spl)
        return render(request, "surveyinterface.html", {'doctorname':doctor[0]['doctorname'],'icon':doctor[0]['picture'], 'specializationid': doctor[0]['specialization'],'splname':spl[0]['specialization']})
    except Exception as e:
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print(e)


def UserQuestions(request):
    try:
        splid=request.GET['splid']
        db, cmd = Pool.ConnectionPooling()
        '''
        SELECT Q.*,group_concat(S.subquestion SEPARATOR '#') FROM medassist.questions Q,subquestions S where Q.questionnumber=S.questionid group by Q.questionnumber;
        '''
        q = "select q.*,(select specialization from specialization where specializationid={0}) as specialization from questions q  where specializationid='{0}';".format(splid)
        cmd.execute(q)
        question = cmd.fetchall()
        q = "select * from subquestions where specializationid='{}'".format(splid)
        cmd.execute(q)
        subquestion = cmd.fetchall()
        print(subquestion)
        return JsonResponse({'result': question,'result2':subquestion})
    except Exception as e:
        print(e)
        return JsonResponse({'result': " "})

def UserQuestionInterface(request):

    splid=request.POST['splid']
    print("????????????????????????????????????????????")
    print(splid)
    return render(request, "UserQuestions.html",{'splid':splid})

def SubmitScore(request):
    try:
        score=json.loads(request.GET['score'])
        print("xxxxxxxxxxxxxxxxxxx",score)
        db, cmd = Pool.ConnectionPooling()
        today = date.today()
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)

        q = "insert into userdoctor(mobileno,doctorid,currentdate,currenttime)values('{}',{},'{}','{}')".format(request.session['user'][1],request.session['doctor'],today,current_time)
        cmd.execute(q)
        db.commit()
        cmd.execute('SELECT last_insert_id() as userdoctorid')
        row=cmd.fetchone()
        print ("IDDDD",row)
        qn=1
        for scr in score:
            L=list(map(int,scr.values()))
            v=sum(L)

            q="insert into userdiagnose(userdoctorid,questionno,totalscore,maxscore) values({},{},{},{})".format(row['userdoctorid'],qn,v,len(L)*5)
            cmd.execute(q)
            qn+=1
        db.commit()
        db.close()
        return JsonResponse({'result':True,'username':request.session['user'][0],'mobileno':request.session['user'][1],'email':request.session['user'][2]})
    except Exception as e:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(e)
        return JsonResponse({'result': False})

#Help
def HelpUserQuestion(request):
    try:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        splid=str(request.GET['splid'])
        print(splid)
        db, cmd = Pool.ConnectionPooling()
        q = "select q.*,(select specialization from specialization where specializationid={0}) as specialization from questions q  where specializationid={0}".format(splid)
        print(q)
        cmd.execute(q)
        question = cmd.fetchall()

        return JsonResponse({"result":question }, safe=False)
    except Exception as e:
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print(e)
        return JsonResponse({"result":[] }, safe=False)

def CallHelpUserQuestion(request):
    return render(request,'HelpUserQuestion.html')
