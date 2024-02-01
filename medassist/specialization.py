from django.shortcuts import render
from django.http import JsonResponse
from . import Pool

from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def specializationInterface(request):
  try:
   admin=request.session['admin']
   print("ADMIN",admin)
   return render(request,"specialization.html",{'msg':''})
  except Exception as e:
   return render(request, "AdminLogin.html", {'msg': ''})


@xframe_options_exempt
def EditSpecialization(request):
    return render(request,"specializationdisplayall.html",{'msg':'Updated'})

@xframe_options_exempt
def specializationDisplayAll(request):
    try:
        db,cmd=Pool.ConnectionPooling()
        q="select * from specialization"
        cmd.execute(q)
        records=cmd.fetchall()
        print(records)
        db.close()
        return render(request, "specializationdisplayall.html", {'result': records,'msg':''})
    except Exception as e:
        print(e)
        return render(request,"specializationdisplayall.html",{'result':'','msg':''})

@xframe_options_exempt
def specializationsubmit(request):
    try:
        db,cmd=Pool.ConnectionPooling()
        specialization=request.POST['specialization']
        iconfile=request.FILES['icon']

        q="insert into specialization (specialization,icon) values('{0}','{1}')".format(specialization,iconfile.name)

        print(q)
        cmd.execute(q)
        db.commit()

        f=open("D:/medassist/assets/"+iconfile.name,"wb")
        for chunk in iconfile.chunks():
            f.write(chunk)
        f.close()
        db.close()
        return render(request, "specialization.html", {'msg': 'record submitted'})
    except Exception as e:
        print(e)
        return render(request,"specialization.html",{'msg':'fail to submit record'})

@xframe_options_exempt
def UpdateSpecialization(request):
    try:
        db,cmd=Pool.ConnectionPooling()

        specializationid = request.GET['specializationid']
        specialization=request.GET['specialization']


        q="update specialization set specialization='{0}' where specializationid={1}".format(specialization, specializationid)

        cmd.execute(q)
        db.commit()
        db.close()
        return JsonResponse({"result":True,},safe=False)
    except Exception as e:
        print(e)
        return JsonResponse({"result":False,},safe=False)

@xframe_options_exempt
def DeleteSpecialization(request):
    try:
        db,cmd=Pool.ConnectionPooling()

        specializationid = request.GET['specializationid']

        q="delete from specialization where specializationid={0}".format(specializationid)

        cmd.execute(q)
        db.commit()
        db.close()
        return JsonResponse({"result":True,},safe=False)
    except Exception as e:
        print(e)
        return JsonResponse({"result":False,},safe=False)

@xframe_options_exempt
def SpecializationDisplayAllJSON(request):
    try:
        db, cmd = Pool.ConnectionPooling()
        q = "select * from specialization"
        cmd.execute(q)
        records=cmd.fetchall()

        db.close()
        return JsonResponse({"result": records, }, safe=False)
    except Exception as e:
        print(e)
        return JsonResponse({"result": {}, }, safe=False)


