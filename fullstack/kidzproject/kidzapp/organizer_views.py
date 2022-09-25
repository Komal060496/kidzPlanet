from django.shortcuts import render,HttpResponse,redirect
from .models import Organizer,Activity_Models,Feedback
from django.views import View
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.http import JsonResponse
# def demo(request):
#     print("Hello")
#     return HttpResponse(request,"<h1>hello</h1>")    
def organizer_reg(request):
        # return HttpResponse("<h1> hello </h1>")
    if request.method == "GET":
        return render(request,'kidzapp/organizer/organizer_reg.html')

    if request.method == "POST":
        # print(request.POST)#built in dictionary
        cusername=request.POST["txtusername"]
        cpassword = request.POST["txtpassword"]
        cname=request.POST["txtname"]
        cemail = request.POST["txtemail"]
        cphone=request.POST["txtnumber"]
        ccity= request.POST["txtcity"]
        caddress=request.POST["txtaddress"]
        # print(cemail,cpassword)
        reg=Organizer(user_name=cusername,password=cpassword,name=cname,email=cemail,phone=cphone,city=ccity,address=caddress)#contactus class ka object creat kar rahe
        reg.save()
        print("Registed")
        messages.success(request,"Thanks You")
    return render(request,'kidzapp/organizer/organizer_reg.html')
def org_login(request):
    if request.method == "GET":
        return render(request,'kidzapp/organizer/org_login.html')
    if request.method == "POST":
        username=request.POST["txtusername"]
        userpass= request.POST["txtpassword"]
        p=Organizer.objects.filter(user_name=username,password=userpass)
        if len(p)>0:
            request.session["user_key"]=username
            request.session["user_type"]="organizer"
             #this is a query to single object form queryset.
            user_object=Organizer.objects.get(user_name=username)
            context={
                "userdata": user_object
            }
            return render(request,'kidzapp/organizer/org_home.html',context)
            
        else:
            messages.error(request,"Invalid Credentials")  
            return redirect('/org_login')
def org_logout(request):
    del request.session["user_key"]
    return redirect("org_login")
def org_editProfile(request):
    if "user_key" in request.session.keys():
    
        loggedinuser_name=request.session["user_key"]
        if request.method == "GET":
            user_object=Organizer.objects.get(user_name=loggedinuser_name)
            context={
                "userdata":user_object
                 }
            return render(request,'kidzapp/organizer/org_editProfile.html',context) 
    else:
            messages.error(request,"Please the fristly login")
            return redirect('home')    
        
    if request.method == "POST":
        name=request.POST["txtusername"]
        emailid=request.POST["txtemail"]
        phonenumber= request.POST["txtphone"]
        user_object=Organizer.objects.get(user_name=loggedinuser_name)
        user_object.name=name
        user_object.email=emailid
        user_object.phone=phonenumber
        # print(name,emailid,phonenumber)
        user_object.save()
        context={
            "userdata":user_object
                 }
        messages.success(request,"Profile updated successfully")
        return render(request,'kidzapp/organizer/org_editProfile.html',context) 
class Add_Activity(View):
    def get(self,request):
        if "user_key" in request.session.keys():#this check the user enter after login.
            user_role=request.session["user_type"]
        #print(user_role)
            # if user_role=='parent':
            #     return render(request,'kidzapp/parent/compose_message.html')
            if user_role=='organizer':
                return render(request,'kidzapp/organizer/add_activity.html')
        else:
            messages.error(request,"Please the fristly login")
            return redirect('home')
    def post(self,request):
            user_name=request.session["user_key"]
            name=request.POST["activity_name"]
            age=request.POST["age_grp"]
            fees=request.POST["fees"]
            duration=request.POST["duration"]
            org=Organizer.objects.get(user_name= user_name)
            add_activity=Activity_Models(user_name=org,activity_name=name,age_group=age,fees=fees,duration=duration)
            add_activity.save()
            context={
                "userdata":add_activity
            }
            messages.success(request,"Your Activity is add successfully")
            return render(request,'kidzapp/organizer/add_activity.html',context)
class View_Feedback(View):
    def get(self, request):
        if "user_key" in request.session.keys():
            user_name=request.session.get("user_key")
            feedback_obj=Feedback.objects.filter(organization_name=user_name)
            context={
                "userdata":feedback_obj
                }
            return render(request,'kidzapp/organizer/org_view_feedback.html',context)
def validate_username1(request): 
    username=request.GET["username"] 
    # jo ye "username"hai vo $.ajax({
    #         url: "/validate_username/",
    #         data:{
    #             'username': username
    #         },
    data={ "exists":Organizer.objects.filter(user_name__iexact=username).exists()}
    return JsonResponse(data)
# class Organizer_Upload_Pic(View):
#     def post(self,request):
#         # print("in post")
#         logged_in_user =request.session["user_key"]
#         org_pic= request.FILES["file_upload"]
#         # print("fileupload",org_pic)
#         fs=FileSystemStorage()
#         file_obj=fs.save(org_pic.name,org_pic)
#         print("name",org_pic.name)
#         print("fileobj",file_obj)
#         print("base",fs.base_url)
#         uploaded_file_url=fs.url(file_obj)
#         print("file url is ",uploaded_file_url)
#         org_object=Organizer.objects.get(user_name=logged_in_user)
#         org_object.pic_name=org_pic.name
#         org_object.save()
#         context={
#             "userdata":org_object,
#             "file_url":uploaded_file_url
                
#         }
#         return render(request,'kidzapp/organizer/org_home.html',context
def  upload_pic(request):
          print("in post method")
          logged_in_user = request.session["user_key"]
          org_pic=request.FILES["file_upload"]
          print("fileupload",org_pic)
          fs=FileSystemStorage()
          file_obj=fs.save(org_pic.name,org_pic)
          print("name",org_pic.name)
          print("fileobj",file_obj)
          print("base",fs.base_url)
          uploaded_file_url=fs.url(file_obj)
          print("file urls is ",uploaded_file_url)
          org_object=Organizer.objects.get(user_name=logged_in_user)
          org_object.pic_name=org_pic.name
          org_object.save()
          context={
            "userdata":org_object,
            "file_url":uploaded_file_url
           }
          return render(request,'kidzapp/organizer/org_home.html',context)
        
        
     
            
        
    
    
    
    
         
         
  