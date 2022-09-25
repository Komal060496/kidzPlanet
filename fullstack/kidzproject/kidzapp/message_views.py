from django.shortcuts import render,HttpResponse,redirect
from .models import User_Message,Parent,Organizer
from django.views import View
from django.contrib import messages

class Compose_Message(View):
    def get(self,request):
        
        if "user_key" in request.session.keys():#this check the user enter after login.
            
        
            user_role=request.session["user_type"]
        #print(user_role)
            if user_role=='parent':
                return render(request,'kidzapp/parent/compose_message.html')
            if user_role=='organizer':
                return render(request,'kidzapp/organizer/compose_message.html')
        else:
            messages.error(request,"Please the fristly login")
            return redirect('home')    
        
    def post(self,request):
            user_role=request.session["user_type"]
            receiver_id=request.POST["txtreceiverid"]
            sender_id=request.session["user_key"]
            subject=request.POST["txtsubject"]
            message_content=request.POST["txtcontent"]
            user_msg=User_Message(receiver_id=receiver_id,sender_id=sender_id,subject=subject,content=message_content)
            user_msg.save()
            if user_role=="parent":
                messages.success(request,"Thank you for message")
                return render(request,'kidzapp/parent/compose_message.html')
            if user_role=="organizer":
                messages.success(request,"Thank you for message")
                return render(request,'kidzapp/organizer/compose_message.html')

class User_Inbox(View):
    def get(self,request):
        if "user_key" in request.session.keys():
            user_id = request.session["user_key"]
            user_role=request.session["user_type"]
            message_objects =User_Message.objects.filter(receiver_id=user_id)
            print(message_objects)
            context={
                "msg": message_objects
            }
        #print(user_role)
            if user_role=='parent':
                return render(request,'kidzapp/parent/parent_inbox.html',context)
            if user_role=='organizer':
                return render(request,'kidzapp/organizer/org_inbox.html',context)
        else:
            messages.error(request,"Please the fristly login")
            return redirect('home')
class Delete_Message(View):
    def post(self, request):
        user_id = request.session["user_key"]
        user_role=request.session["user_type"]
        message_objects_list=request.POST.getlist("chk")
        # print(message_objects_list)
        for msg_id in message_objects_list:
            # print(msg_id)
            msg_objects=User_Message.objects.get(id=msg_id)
            msg_objects.delete()
        message_objects=User_Message.objects.filter(receiver_id=user_id) 
        context={
                "msg": message_objects
            }
        #print(user_role)
        if user_role=='parent':
                return render(request,'kidzapp/parent/parent_inbox.html',context)
        if user_role=='organizer':
                return render(request,'kidzapp/organizer/org_inbox.html',context)
class Show_Message(View):
    def get(self, request,msg_id):
        user_id = request.session["user_key"]
        user_role=request.session["user_type"]
        message_object=User_Message.objects.get(id=msg_id)
        print(message_object)
        context={
                "msg": message_object
            }
        #print(user_role)
        if user_role=='parent':
                return render(request,'kidzapp/parent/parent_showmessage.html',context)
        if user_role=='organizer':
                return render(request,'kidzapp/organizer/org_showmessage.html',context)
            
            
           

        
    
                  
               
            