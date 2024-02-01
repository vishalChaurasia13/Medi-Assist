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

from . import specialization, DoctorRegistration, Questions, SubQuestions, AdminLogin, UserRegistration



urlpatterns = [

# specialization
    path('admin/', admin.site.urls),
    path('specialization/',specialization.specializationInterface),
    path('editSpecialization/',specialization.EditSpecialization),
    path('SpecializationSubmit',specialization.specializationsubmit),
    path('specializationDisplayAll/',specialization.specializationDisplayAll),
    path('specializationdisplayallJSON/',specialization.SpecializationDisplayAllJSON),
    path('updatespecialization/', specialization.UpdateSpecialization),
    path('deletespecialization/', specialization.DeleteSpecialization),

# Doctors.......................
    path('doctorregistration/', DoctorRegistration.DoctorRegisterInterface),
    path('doctorregistred', DoctorRegistration.DoctorRegistred),
    path('doctorrecorddisplay/', DoctorRegistration.DoctorRecordDisplay),
    path('doctorrecordupdate/', DoctorRegistration.DoctorRecordupdate),
    path('deletedoctor/', DoctorRegistration.DeleteDoctor),
    path('editdoctoricon', DoctorRegistration.EditDoctorIcon),

#Questions....................
    path('questioninterface/', Questions.QuestionInterface),
    path('questionsubmit/', Questions.QuestionSubmit),
    path('questionjson/', Questions.QuestionJSON),

#Sub-Questions................
    path('subquestioninterface/', SubQuestions.SubQuestionInterface),
    path('subquestionsubmit/', SubQuestions.SubQuestionSubmit),

#Admin....................
    path('adminlogin/', AdminLogin.AdminLogin),
    path('adminlogout/', AdminLogin.AdminLogout),
    path('dashboard', AdminLogin.CheckAdminLogin),

# User Details------------------------
    path('userregistration/', UserRegistration.UserRegistrationInterface),
    path('loginpage/', UserRegistration.UserLogin),
    path('otppage', UserRegistration.OtpPage),
    path('userregistrationsubmit', UserRegistration.UserRegistrationSubmit),
    path('userregistrationdisplayall/', UserRegistration.UserRegistrationDisplayAll),
    path('userlogininterface/', UserRegistration.UserLoginInterface),
    path('emaillogin/', UserRegistration.EmailLogin),
    path('forgetpassword/', UserRegistration.ForgetPassword),
    path('checkemailidandpasswd',UserRegistration.CheckEmailIdAndPasswd),
    path('checkotp',UserRegistration.ChkOtp),
    path('womacform/', UserRegistration.WomacForm),
    path('surveyinterface',UserRegistration.SurveyInterface),
    path('userquestions/',UserRegistration.UserQuestions),
    path('userquestion',UserRegistration.UserQuestionInterface),
    path('submitscore/',UserRegistration.SubmitScore),

    path('helpuserquestion/', UserRegistration.HelpUserQuestion),
    path('callhelpuserquestion/', UserRegistration.CallHelpUserQuestion),

]
