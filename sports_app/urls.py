from django.urls import path,include
from.import views,user_views
urlpatterns = [
   path("",views.home,name="home"),
   path("contactus/",views.contactus,name="contactus"),
   path("aboutus/",views.aboutus,name="aboutus"),
   path("feedback/",user_views.feedback,name="feedback"),
   path("user_login/",user_views.user_login,name='user_login'),
   path("Registration/",user_views.Registration,name='Registration'),
   path("user_home/",user_views.user_home,name='user_home'),
   path("user_logout/",user_views.user_logout,name='user_logout'),
   path("view_courses/",views.view_courses,name='view_courses'),
   path("view_coach/",views.view_coach,name='view_coach'),
   path("user_coach/",user_views.user_coach,name='user_coach'),
   path("admission/",user_views.admission,name='admission'),
   path("admission_status/",user_views.admission_status,name='admission_status'),
   path("user_editprofile/",user_views.user_editprofile,name='user_editprofile'),
   path("about_athletics/",views.about_athletics,name='about_athletics'),
   path("about_badminton/",views.about_badminton,name='about_badminton'),
   path("about_cricket/",views.about_cricket,name='about_cricket'),
   path("about_swimming/",views.about_swimming,name='about_swimming')

]

