from django.shortcuts import render
from . import Pool

def RegistrationInterface(request):
    return render(request,"registration.html", {'msg': ''})


def registrationsubmit(request):
    try:
        db,cmd=Pool.ConnectionPooling()


        doctorname=request.POST['doctorname']
        dob= request.POST['dob']
        gender= request.POST['gender']
        mobileno= request.POST['mobileno']
        emailaddress= request.POST['emailaddress']
        specialization=request.POST['specialization']
        iconfile = request.FILES['icon']


        q="insert into registration(doctorname,dob,gender,mobileno,emailaddress,specialization,icon) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(doctorname,dob,gender,mobileno,emailaddress,specialization,iconfile.name)

        print(q)
        cmd.execute(q)
        db.commit()

        f=open("D:/medassist/assets/"+iconfile.name,"wb")
        for chunk in iconfile.chunks():
            f.write(chunk)
        f.close()
        db.close()
        return render(request, "registration.html", {'msg': 'Registered'})
    except Exception as e:
        print(e)
        return render(request,"registration.html",{'msg':'Something went wrong !!!'})
