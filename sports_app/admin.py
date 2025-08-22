from django.contrib import admin
from .models import Contact,FeedBack,User,SportsCourse,Coach,AdmissionForm,Notice


class Contact_Admin(admin.ModelAdmin):
    
    list_display = ["name","email","phone","query","date"] 

class Feedback_Admin(admin.ModelAdmin):
    
    list_display1 = ["name","email","rating","remark","date"] 


admin.site.register(Contact,Contact_Admin)
admin.site.register(FeedBack,Feedback_Admin)
admin.site.register(User)
admin.site.register(SportsCourse)
admin.site.register(Coach)
admin.site.register(AdmissionForm)
admin.site.register(Notice)



admin.site.site_header="Sports Academy Admin Dashboard"

admin.site.site_title = "Where every yard tells a story of hustle and glory"

admin.site.index_title = "THE 22 YARD CLUB"