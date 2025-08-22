from django.shortcuts import render,redirect
from .models import Contact,User,SportsCourse,FeedBack,Coach,Notice
from django.contrib import messages

# Create your views here.
def about_athletics(request):
    return render(request,"sports_app/html/about_athletics.html")

def about_badminton(request):
    return render(request,"sports_app/html/about_badminton.html")

def about_cricket(request):
    return render(request,"sports_app/html/about_cricket.html")

def about_swimming(request):
    return render(request,"sports_app/html/about_swimming.html")

def view_coach(request):
    coach_list=Coach.objects.all()
    context={
        "coach_key":coach_list
    }
    return render(request,"sports_app/html/view_coach.html",context)


def view_courses(request):
    course_list=SportsCourse.objects.all()
    context={
        "course_key":course_list
    }
    return render(request,"sports_app/html/view_courses.html",context)  # context is used to send dict to html page


def home(request):
  
     notice_list= Notice.objects.all()
  
  
  
   #for showing feedback with profile pic on home page 


     feedback = FeedBack.objects.all()
     data=[]
     for f in feedback:
         data.append(
             {
                 
                  'rating':f.rating,
                  "remarks":f.remarks,
                  'name':f.name,
                  "profile_pic":User.objects.filter(email=f.email)[0].profile_pic         
             }      
         )
     feedback_dict={
        "feedback_key":data,
        "notice_key":notice_list
    }
      
     return render(request,'sports_app/html/index.html',feedback_dict)







def contactus(request):
   
    
    if request.method=='GET':
        return render(request,'sports_app/html/contactus.html')
     
    if request.method=='POST': 
      user_name=request.POST['name']
      user_email=request.POST['email']
      user_phone=request.POST['phone']
      user_question=request.POST['question']
      user_contact=Contact(name=user_name,email=user_email,phone=user_phone,query=user_question)
      user_contact.save()

      messages.success(request, 'WE WILL CONTACT YOU ASAP') 
      return redirect("/contactus/")


def aboutus(request):
    return render(request,"sports_app/html/aboutus.html")
