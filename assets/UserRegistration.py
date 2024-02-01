from django.shortcuts import render,redirect
from . import Pool
import datetime
import re
from django.http import JsonResponse
import random
import json

class dataerror(Exception):
    pass


errors=[]
error1=[]

def checkpassword(password):
    if 6<=len(password)<=12:
        if re.search("[a-z]",password):
            if re.search("[A-Z]", password):
                if re.search("[0-1]", password):
                    if re.search("[!@#$%^&*)(+=._-]", password):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def checkemail(email):
    regex = '^[a-zA-Z]+[\._]?[a-z0-9A-Z]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        return True
    else:
        return False

def checkmobileno(mobile):
    if len(mobile)==10:
        return True
    else:
        return False

def UserLoginInterface(request):
    return render(request, "UserLoginInterface.html", {'msg': ""})

def EmailLogin(request):
    return render(request, "EmailLogin.html")


def UserLogin(request):
    return render(request, "LoginPage.html")

def CheckOtp(request):
    try:
        gotp=request.POST['gotp']
        d1=request.POST['digit1']
        d2 = request.POST['digit2']
        d3 = request.POST['digit3']
        d4 = request.POST['digit4']
        if gotp==d1+d2+d3+d4:
            return redirect('womacform/')
        else:
            return render(request, "OTPverification.html", {'msg': "Incorrect OTP", 'gotp': gotp})
    except Exception as e:
        print(e)
        return render(request, "OTPverification.html", {'msg': "Incorrect OTP", 'gotp': gotp})




def OTPVerification(request):
    try:
        mobno = request.POST['mobileno']
        db, cmd = Pool.ConnectionPooling()
        q = "Select * from userregistration where mobileno='{}'".format(mobno)
        cmd.execute(q)
        data = cmd.fetchall()
        if data==():
            return render(request, "LoginPage.html",{'msg':'Invalid Mobile Number'})
        else:
            otp=random.randint(1000,9999)
            print(otp)
            return render(request, "OTPverification.html",{'msg':"",'gotp':otp})

    except Exception as e:
        print(e)
        return render(request, "LoginPage.html",{'msg':''})

def UserRegister(request):
    return render(request,"UserRegistration.html",{'msg':""})

def ForgetPassword(request):
    return render(request, "ForgetPassword.html", {'msg': ""})

def SubmitUserRecord(request):
    global errors,error1
    try:
        print("In Submit Record Function")
        db, cmd = Pool.ConnectionPooling()
        username=request.GET['username']
        state= request.GET['state']
        city=request.GET['city']
        email = request.GET['email']
        mobileno = request.GET['mobileno']
        dob = request.GET['dob']
        dor = request.GET['dor']
        password = request.GET['password']

        if not checkemail(email):
            errors.append("email")

        if not checkmobileno(mobileno):
            errors.append("mobileno")

        if not checkpassword(password):
            errors.append("password")

        print(checkmobileno(mobileno), checkpassword(password), errors)
        if len(errors)!=0:
            error1= errors.copy()
            errors=[]
            raise dataerror

        print(username,state,city,email,mobileno,dob,dor,password)
        q= "insert into userregistration(username,state,city,emailid,mobileno,dateofbirth,dateofregistration,password) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(username,state,city,email.lower(),mobileno,dob,dor,password)
        cmd.execute(q)
        db.commit()
        db.close()
        return JsonResponse({'result':True},safe=False)

    except dataerror as e:
        print("Data Error in Submit Record Function")
        print(e)
        return JsonResponse({'result': False,'error':error1}, safe=False)

    except Exception as e:
        print("Server Error in Submit Record Function")
        print(e)
        return JsonResponse({'result': False,'servererror':True}, safe=False)


def WomacForm(request):
    try:
        db,cmd= Pool.ConnectionPooling()
        q="Select * from doctorregistration"
        cmd.execute(q)
        data=cmd.fetchall()
        return render(request, "WomacSurveys.html", {'msg': "",'Data':data})
    except Exception as e:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(e)
        return render(request, "WomacSurveys.html", {'msg': ""})

""" def UserQuestion(request):
    try:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        splid=str(request.POST['splid'])
        print(splid)
        db, cmd = Pool.ConnectionPooling()
        q = "select q.*,(select specialization from specialization where specializationid={0}) as specialization from questions q  where specializationid={0}".format(splid)
        print(q)
        cmd.execute(q)
        question = cmd.fetchall()
        qlength=len(question)
        q = "Select * from subquestions where questionid={0}".format(question[0]['questionid'])
        cmd.execute(q)
        subquestion = cmd.fetchall()
        print(subquestion)
        return render(request, "UserQuestionsPrev.html", {'question':question[0],'subquestion':subquestion,'length':len(subquestion),'qnum':0,'scorelist':[],'qlength':qlength,'splid':splid,'splname':question[0]['specialization']})
    except Exception as e:
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print(e)
        return render(request, "UserQuestionsPrev.html", {'question':[], 'subquestion': []})

def UserQuestion2(request):
    try:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        splid = request.POST['splid']
        scorelist=request.POST['scorelist']
        qnum= int(request.POST['qnum'])
        scorelist=request.POST['scorelist']
        prevlist = list(request.POST['prevlist'].split(" "))
        prevlist.append(scorelist)
        prevlist=" ".join(prevlist)
        db, cmd = Pool.ConnectionPooling()
        q = "select q.*,(select specialization from specialization where specializationid={0}) as specialization from questions q  where specializationid='{0}';".format(splid)
        cmd.execute(q)
        question = cmd.fetchall()
        qlength = len(question)
        qlen=len(question)-1
        if qnum<=qlen:
            q = "Select * from subquestions where questionid={}".format(question[qnum]['questionid'])
            cmd.execute(q)
            subquestion = cmd.fetchall()
            print(subquestion)
            return render(request, "UserQuestionsPrev.html", {'question':question[qnum],'subquestion':subquestion,'length':len(subquestion),'qnum':qnum,'scorelist':"",'prevlist':prevlist,'qlength':qlength,'splid':splid,'splname':question[0]['specialization']})
        else:
            return render(request, "nextpage.html",{'prevlist':prevlist})
    except Exception as e:
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print(e)
        return render(request, "UserQuestionsPrev.html", {'question':[], 'subquestion': []})

def PrevQuestion(request):
    try:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        splid = request.POST['splid']
        scorelist=request.POST['scorelist']
        qnum= int(request.POST['qnum'])-2
        prevlist = list(request.POST['prevlist'].split(" "))
        print(prevlist)
        scorelist=prevlist[-1]
        prevlist=prevlist[0:len(prevlist)-1]
        prevlist=" ".join(prevlist)
        print(prevlist)
        print(scorelist)
        db, cmd = Pool.ConnectionPooling()
        q = "select q.*,(select specialization from specialization where specializationid={0}) as specialization from questions q  where specializationid='{0}';".format(splid)
        cmd.execute(q)
        question = cmd.fetchall()
        qlength = len(question)
        qlen=len(question)-1
        q = "Select * from subquestions where questionid={}".format(question[qnum]['questionid'])
        cmd.execute(q)
        subquestion = cmd.fetchall()
        print(subquestion)
        return render(request, "UserQuestionsPrev.html", {'question':question[qnum],'subquestion':subquestion,'length':len(subquestion),'qnum':qnum,'scorelist':scorelist,'prevlist':prevlist,'qlength':qlength,'splid':splid,'splname':question[0]['specialization']})
    except Exception as e:
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print(e)
        return render(request, "UserQuestionsPrev.html", {'question':[], 'subquestion': []})


"""
def SurveyInterface(request):
    try:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        sid=request.POST['sid']
        db, cmd = Pool.ConnectionPooling()
        q = "Select * from doctorregistration where doctorid='{0}'".format(sid)
        cmd.execute(q)
        doctor = cmd.fetchall()
        print(doctor)
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
        q = "select q.*,(select specialization from specialization where specializationid={0}) as specialization from questions q  where specializationid='{0}';".format(splid)
        cmd.execute(q)
        question = cmd.fetchall()
        q = "select * from subquestions"
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
        score=request.GET['score']
        print(score)
       # JsonResponse()
        return JsonResponse({'result':True})
    except Exception as e:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(e)
        return JsonResponse({'result':False})



