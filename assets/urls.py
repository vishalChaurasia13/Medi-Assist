"""medassist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from.import Specialization
from.import DoctorRegistration
from.import UserRegistration
from.import Admin

urlpatterns = [
    path('admin/', admin.site.urls),

    #Secialization.......................
    path('specialization/',Specialization.SpecializationInterface),
    path('specializationsubmit',Specialization.SpecializationSubmit),
    path('specializationrecorddisplay/',Specialization.SpecializationRecordDisplay),
    path('specializationrecorddisplayJSON/',Specialization.SpecializationRecordDisplayJSON),
    path('updatespecialization/',Specialization.UpdateSpecialization),
    path('deletespecialization/',Specialization.DeleteSpecialization),
    path('editspecializationicon',Specialization.EditSpecializationIcon),

    #Doctors.......................
    path('doctorregistration/',DoctorRegistration.DoctorRegisterInterface),
    path('doctorregistred',DoctorRegistration.DoctorRegistred),
    path('doctorrecorddisplay/',DoctorRegistration.DoctorRecordDisplay),
    path('doctorrecordupdate/',DoctorRegistration.DoctorRecordupdate),
    path('deletedoctor/',DoctorRegistration.DeleteDoctor),
    path('editdoctoricon',DoctorRegistration.EditDoctorIcon),

    #UserRegistration.......................
    path('userlogininterface/',UserRegistration.UserLoginInterface),
    path('otplogin/',UserRegistration.UserLogin),
    path('emaillogin/',UserRegistration.EmailLogin),
    path('forgetpassword/',UserRegistration.ForgetPassword),
    path('otpverification',UserRegistration.OTPVerification),
    path('userregistration/',UserRegistration.UserRegister),
    path('submituserrecord/',UserRegistration.SubmitUserRecord),
    path('womacform/',UserRegistration.WomacForm),
    path('checkotp',UserRegistration.CheckOtp),
    #path('userquestion',UserRegistration.UserQuestion),
    #path('userquestion2',UserRegistration.UserQuestion2),
    #path('prevquestion',UserRegistration.PrevQuestion),
    path('surveyinterface',UserRegistration.SurveyInterface),
    path('userquestions/',UserRegistration.UserQuestions),
    path('userquestion',UserRegistration.UserQuestionInterface),
    path('submitscore/',UserRegistration.SubmitScore),



    #Admin...........................................
    path('adminlogin/', Admin.AdminLogin),
    path('dashboard', Admin.Dashboard),

]

