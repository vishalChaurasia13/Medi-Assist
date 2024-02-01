from django.shortcuts import render
from . import Pool
import datetime
from django.http import JsonResponse

from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def DoctorRegisterInterface(request):
    return render(request,"DoctorRegistration.html",{"msg":""})

@xframe_options_exempt
def DoctorRegistred(request):
    try:
        db, cmd = Pool.ConnectionPooling()
        dname=request.POST['dname']
        dob=request.POST['dob']
        gen=request.POST['gender']
        mobnum=request.POST['mobnum']
        email=request.POST['email']
        picfile=request.FILES['pic']
        special=request.POST['special']

        q="Insert into doctorregistration(doctorname,dob,gender,emailaddress,picture,mobile,specialization) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(dname,dob,gen,email,picfile.name,mobnum,special)
        cmd.execute(q)
        db.commit()
        f = open("D:/medassist/assets/"+picfile.name,mode="wb")
        for chunk in picfile.chunks():
            f.write(chunk)
        f.close()
        db.close()
        return render(request, "DoctorRegistration.html", {"msg": "Record Submitted"})
    except Exception as e:
        print("ERROR",e)
        return render(request, "DoctorRegistration.html", {"msg": "Record Failed"})

@xframe_options_exempt
def DoctorRecordDisplay(request):
    try:
        db,cmd=Pool.ConnectionPooling()
        q="Select * From doctorregistration"
        cmd.execute(q)
        data=cmd.fetchall()
        return render(request, "DoctorRecordDisplay.html", {'data':data})

    except Exception as e:
        return render(request, "DoctorRecordDisplay.html", {'msg': " "})


@xframe_options_exempt
def DoctorRecordupdate(request):
    try:
        print("................")
        db,cmd=Pool.ConnectionPooling()
        id=request.GET['did']
        dname=request.GET['dname']
        dob=request.GET['dob']
        email=request.GET['email']
        dnum=request.GET['mnumber']
        dspl=request.GET['dspl']
        q = "update doctorregistration set doctorname='{0}',dob='{1}',emailaddress='{2}',mobile='{3}',specialization='{4}' where doctorid='{5}'".format(dname,dob,email,dnum,dspl,id)
        cmd.execute(q)
        db.commit()
        db.close()
        return JsonResponse({'result':True},safe=False)

    except Exception as E:
        print("................")
        print(E)
        return JsonResponse({'result':False},safe=False)

@xframe_options_exempt
def DeleteDoctor(request):
    try:
        print("................")
        db,cmd=Pool.ConnectionPooling()
        id=request.GET['did']
        q = "delete from doctorregistration where doctorid='{0}'".format(id)
        cmd.execute(q)
        db.commit()
        db.close()
        return JsonResponse({'result':True},safe=False)

    except Exception as E:
        print("................")
        print(E)
        return JsonResponse({'result':False},safe=False)

@xframe_options_exempt
def EditDoctorIcon(request):
    try:
        db, cmd = Pool.ConnectionPooling()
        id = request.POST['id']
        picfile = request.FILES['icon']
        q="update doctorregistration set picture='{0}' where doctorid='{1}'".format(picfile,id)
        cmd.execute(q)
        db.commit()
        f = open("D:/medassist/assets/" + picfile.name, mode="wb")
        for chunk in picfile.chunks():
            f.write(chunk)
        f.close()
        db.close()
        return JsonResponse({'result': True}, safe=False)
    except Exception as e:
        print(e)
        return JsonResponse({'result': False}, safe=False)


