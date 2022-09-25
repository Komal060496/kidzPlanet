from django.shortcuts import render,HttpResponse,redirect
from .models import Activity_Models, CityEvent, Contact, Parent,Admission,Organizer,Feedback,Prediction
from django.contrib import messages
from django.views import View
from django.http import JsonResponse
from django.db.models import Q
from sklearn.tree import DecisionTreeClassifier
import joblib
import pandas as pd
from django.views.decorators.cache import cache_control



def home(request):
    # return HttpResponse("<h1> hello </h1>")
    # data_dict={
    #     "info":"Data from view"
    # }
    events=CityEvent.objects.all()
    context={
        "info":events
    }
    return render(request,'kidzapp/html/home.html',context)

def aboutus(request):
    # return HttpResponse("<h1> hello </h1>")
    return render(request,'kidzapp/html/aboutus.html')




def contactus(request):
    # return HttpResponse("<h1> hello </h1>")
    if request.method == "GET":
        return render(request,'kidzapp/html/contactus.html')

    if request.method == "POST":
        # print(request.POST)#built in dictionary
        cname = request.POST["txtname"]
        cemail = request.POST["txtemail"]
        cphone = request.POST["txtphone"]
        cquery= request.POST["txtquery"]
        # print(cname,cemail,cemail,cphone,cquery)
        contact=Contact(name=cname,email=cemail,phone=cphone,your_query=cquery)#contactus class ka object creat kar rahe
        contact.save()
        print("Contact saved")
        messages.success(request,"Thanks You")
    return render(request,'kidzapp/html/contactus.html') 
  
def login(request):
    if request.method == "GET":
        return render(request,'kidzapp/parent/login.html')
    if request.method == "POST":
        username=request.POST["txtusername"]
        userpass= request.POST["txtpassword"]
        p=Parent.objects.filter(user_name=username,password=userpass)
        if len(p)>0:
            request.session["user_key"]=username
            request.session["user_type"]="parent"
            #this is a query to single object form queryset.
            user_object=Parent.objects.get(user_name=username)
            context={
                "userdata": user_object
            }
            return render(request,'kidzapp/parent/parent_home.html',context)
        else:
            messages.error(request,"Invalid Credentials")  
            return redirect('login')
         

def parent_reg(request):
    # return HttpResponse("<h1> hello </h1>")
    if request.method == "GET":
        return render(request,'kidzapp/parent/parent_reg.html')

    if request.method == "POST":
        # print(request.POST)#built in dictionary
        cusername=request.POST["txtusername"]
        cpassword = request.POST["txtpassword"]
        cname=request.POST["txtname"]
        cemail = request.POST["txtemail"]
        cphone=request.POST["txtphone"]
        # print(cusername,cemail,cpassword)
        login=Parent(user_name=cusername,password=cpassword,name=cname,email=cemail,phone=cphone)#contactus class ka object creat kar rahe
        login.save()
        messages.success(request,"Thanks You")
        print("Contact saved")
    return render(request,'kidzapp/parent/parent_reg.html')
#--logout
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def parent_logout(request):
    del request.session["user_key"]
    return redirect("login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def parent_editProfile(request):
    if "user_key" in request.session.keys():
        loggedinuser_name=request.session["user_key"]
        if request.method == "GET":
            user_object=Parent.objects.get(user_name=loggedinuser_name)
        
            context={
                "userdata":user_object
                  }
            return render(request,'kidzapp/parent/parent_editProfile.html',context)
    else:
            messages.error(request,"Please login first")
            return redirect('home')      
    if request.method == "POST":
        emailid=request.POST["txtemail"]
        phonenumber= request.POST["txtphone"]
        user_object=Parent.objects.get(user_name=loggedinuser_name)
        user_object.email=emailid
        user_object.phone=phonenumber
        print(emailid,phonenumber)
        user_object.save()
        context={
            "userdata":user_object
                 }
        messages.success(request,"Profile updated successfully")
        return render(request,'kidzapp/parent/parent_editProfile.html',context)

class Enrollment_Form(View):
     def get(self, request,p_id):
         if "user_key" in request.session.keys():
             prg_id=p_id
             user_id = request.session["user_key"]
        
             admission=Activity_Models.objects.get(id=p_id)
             context={
                "admission": admission
                 }
             return render(request,'kidzapp/parent/admission.html',context)
         else:
                messages.error(request,"Please the fristly login")
                return redirect('home') 


def final_admission(request):
            actid=request.POST["txtactivity_id"]
            user_name=request.session["user_key"]
            name=request.POST["kid_name"]
            age=request.POST["age"]
            school=request.POST["school_name"]
            mother=request.POST["mothername"]
            father=request.POST["fathername"]
            phone=request.POST["phone_no"]
            fees=request.POST["fees"]
            transaction=request.POST["transaction_id"]
            
            parent_obj=Parent.objects.get(user_name=user_name)
            admission=Admission(activity_id=actid,parent_user_name=parent_obj,kid_name=name,age=age,school_name=school,mother_name=mother,father_name=father,phone_no=phone,transaction_id=transaction)
            admission.save()
            context={
                "userdata":admission
            }
            messages.success(request,"Your Activity is add successfully")
            return render(request,'kidzapp/parent/admission.html',context)   
     
 
     
@cache_control(no_cache=True, must_revalidate=True, no_store=True)   
def trail(request):
    return render(request,'kidzapp/parent/trail.html') 

class Show_Activity(View):
    def get(self, request,username):
             activities=Activity_Models.objects.filter(user_name=username)
             context={
                "ac": activities
                 }
             if "user_key" in request.session.keys():
            #  if user_role=='parent':
                 return render(request,'kidzapp/parent/activities.html',context)
             else:
    
                 return render(request,'kidzapp/html/common_activities.html',context)
                  
class Feed_back(View):
    def get(self, request,username):
       
        if "user_key" in request.session.keys():
             
            #  user_id = request.session["user_key"]
        
             #admission=Organizer.objects.filter(user_name=username)
             context={
                "org_user_name": username
                 }
             return render(request,'kidzapp/parent/feedback.html',context)
def final_feedback(request):
            user_name=request.session["user_key"]
            org_user_name=request.POST["txtorg_user_name"]
            feedback=request.POST["feedback"]
            rating=request.POST["rating"]
            user_object=Parent.objects.get(user_name=user_name)
           
            rt=int(rating)
            p=Parent.objects.get(user_name=user_name)
            
            feedback=Feedback(user_name=p,organization_name=org_user_name,feedback_text=feedback,rating=rt)
            feedback.save()
            
            context={
                "userdata":user_object
            }
            messages.success(request,"Thanks for giving feedback ")
            return render(request,'kidzapp/parent/parent_home.html',context)
            # return render(request,'kidzapp/parent/feedback.html',context)
            # return redirect("")
            # return redirect('parent_home') 
def feed(request):
    # return HttpResponse("<h1> hello </h1>")
    return render(request,'kidzapp/html/feed.html')
           
def view_act(request):
    activity=Organizer.objects.all()
   
    context={
        "act":activity
    }
    if "user_key" in request.session.keys():
        return render(request,'kidzapp/parent/view_activity.html',context)   
    else:
        return render(request,'kidzapp/html/common_view_activity.html',context)   

    
def courses(request):
    user_name=request.session["user_key"]
    admission_obj=Admission.objects.filter(parent_user_name=user_name)
    context={
        "act":admission_obj
    }
    if "user_key" in request.session.keys():
    # return HttpResponse("<h1> hello </h1>")
         return render(request,'kidzapp/parent/purchase.html',context)   
    return render(request,'kidzapp/parent/purchase.html') 



def common_feedback(request):
    feed_obj=Feedback.objects.all()
    context={
             "feedback":feed_obj
            }
    return render(request,'kidzapp/html/common_view_feedback.html',context) 
    
def validate_username(request): 
    username=request.GET["username"] 
    data={ "exists":Parent.objects.filter(user_name__iexact=username).exists()}
    return JsonResponse(data)
def search(request):
    if request.method == "POST":
        txt_search=request.POST["txt_search"]
        sear_obj=Activity_Models.objects.filter(Q(activity_name__contains=txt_search)|Q(age_group__contains=txt_search)|Q( fees__contains=txt_search)|Q(duration__contains=txt_search))
        if len(sear_obj)>0:
            context={
                "search_details":sear_obj
            }
            return render(request,'kidzapp/html/search_box.html',context)
        else:
            messages.error(request,"Give Details is not Found")
            return redirect("home")
        
      
class Predict(View):
    def get(self,request):
        return render(request,'kidzapp/html/ml.html')  
    def post(self,request):
            name=request.POST["txtname"]
            email=request.POST["txtemail"]
            age=request.POST["age"]
            gender=request.POST["gender"]
            playgroup=request.POST["playgroup"]
            ml_model=joblib.load("ml_model/kids_planet_modal.joblib")
            print(ml_model)
            predicted_value=ml_model.predict([[age,gender,playgroup]])
            print(predicted_value)
            context={
                "pre": predicted_value
            }
            pre=Prediction(name=name,email=email,age=age,gender=gender,interest=predicted_value,playgroup=playgroup)
            pre.save()
            messages.success(request,"Thanks")
            
            return render(request,'kidzapp/html/ml.html',context) 
        
class back(View):
     def get(self, request,id):
            # feed_obj=Feedback.objects.all()
            user_objects=Feedback.objects.filter(organization_name=id)
            context={
                     "id":user_objects,
                    #  "x":feed_obj,
                 }
            return render(request,'kidzapp/html/rating.html',context)  
    
                     

