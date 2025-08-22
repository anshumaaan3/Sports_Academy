from django.shortcuts import render , redirect
from .models import User,FeedBack,Coach,SportsCourse,AdmissionForm
from django.contrib import messages

def user_editprofile(request):
   if request.method=="GET":
        user_email=request.session["web_key"]
        user_Obj=User.objects.get(email=user_email)
        user_dict={
        "user_key":user_Obj  
            }
    

        return render(request,"sports_app/user/user_editprofile.html",user_dict)
   if request.method=="POST":
       user_name=request.POST["name"]
       user_phone=request.POST["phone"]
       user_pic=request.FILES.get("pic")
       user_email=request.session["web_key"]
       user_Obj=User.objects.get(email=user_email)
       if user_pic is not None:
          user_Obj.profile_pic=user_pic
       user_Obj.name=user_name
       user_Obj.phone=user_phone
       user_Obj.save()
       messages.success(request,"Profile Updated")   
       return redirect("user_home")

def admission_status(request):
   if request.method=="GET":
        email=request.session["web_key"]
        form_obj=AdmissionForm.objects.get(user_email=email)
        form_dict={
           
               "form_key":form_obj

        }
        return render(request,"sports_app/user/admission_status.html",form_dict)

def admission(request):
   if request.method=='GET':
        user_email=request.session["web_key"]
        course_list=SportsCourse.objects.all()
        context={
                "course_key":course_list,
                "email":user_email
            }
        return render(request,"sports_app/user/admission.html",context)

   if request.method=="POST":
        course_name=request.POST["courses"]
        user_email=request.POST["email"]
        user_name=request.POST["name"]
        dob=request.POST["dob"]
        user_gender=request.POST["gender"]
        user_phone=request.POST["phone"]
        user_address=request.POST["address"]
        user_pic=request.FILES["admission_pic"]

        admission_obj=AdmissionForm(course_name=course_name,user_email=user_email,full_name=user_name,date_of_birth=dob,phone=user_phone,gender=user_gender,address=user_address,pic_name=user_pic)
        admission_obj.save()
        return redirect("admission")




def user_coach(request):
    coach_list=Coach.objects.all()
    context={
        "coach_key":coach_list
    }
    return render(request,"sports_app/user/user_coach.html",context)

def user_logout(request):
   request.session.flush()
   messages.success(request,'logged out')
   return redirect("user_login")


def user_home(request):
# fetching values = email  from session to identify the user
  if request.method=='GET':
    user_email=request.session["web_key"]
    user_Obj=User.objects.get(email=user_email)  #it will return a single object
        # sending data from view to html page
        #  create a dictionary and bind data with key
        # send that dictionary with render function
    user_dict={
            "user_key":user_Obj  
            }
    return render(request,"sports_app/user/user_home.html",user_dict)




def user_login(request):
    if request.method == "GET":
        return render(request, 'sports_app/user/user_login.html')
    
    if request.method == "POST":
        user_email = request.POST["email"]
        user_password = request.POST["password"]

        # select * from user where email = user_email and password = user_password
        user_list = User.objects.filter(email=user_email, password=user_password)

        if len(user_list) > 0:
          
          request.session['web_key']=user_email # binding email in session to track it for multiple requests
          return redirect("user_home")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("user_login")
        


def feedback(request):
    if request.method=="GET":
      return render(request,"sports_app/html/feedback.html")
    
    if request.method=="POST":
        user_name=request.POST["name"]    
        user_email=request.session["web_key"]
        user_rating=request.POST["rating"]
        user_remarks=request.POST["remarks"]
        
        user_obj=FeedBack(name=user_name,email=user_email,rating=user_rating,remarks=user_remarks)
        user_obj.save()
        messages.success(request, 'successfully submitted')


        return redirect("feedback")
    




def Registration(request):
    if request.method=="GET":
     return render(request,"sports_app/user/Registration.html")
    if request.method=="POST":
        user_email= request.POST["email"]   #control name input field
        user_password=request.POST["password"]
        user_name=request.POST["name"]
        user_phone=request.POST["phone"]
        user_pic=request.FILES["profile_pic"]
       
       
        # object relational mapping framework #
        # create object of user model the order in models
        # set values
        # save object -- it automatically stores the value in table

        user_obj=User(name=user_name,email=user_email,password=user_password,phone=user_phone,profile_pic=user_pic)
        user_obj.save()
        return redirect("user_login")