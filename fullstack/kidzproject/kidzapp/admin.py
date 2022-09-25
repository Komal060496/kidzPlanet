from django.contrib import admin


from kidzapp.organizer_views import Add_Activity
from .models import Activity_Models, Contact, CityEvent,Feedback, Organizer,Parent, User_Message,Activity_Models

class OrganizerAdmin(admin.ModelAdmin):
    list_display =('user_name','name','email','phone','city','address')
    list_filter =['name','city']
    search_fields =('city',)
class ParentAdmin(admin.ModelAdmin):
    list_display =('user_name','name','email','phone')

class ContactAdmin(admin.ModelAdmin):
    list_display =('name','email','phone','your_query')  
    list_filter =['name','your_query'] 
class FeedbackAdmin(admin.ModelAdmin):
    list_display =('user_name','organization_name','feedback_text','rating','date')   
    list_filter =['organization_name','rating']
    search_fields=('rating',)
class Activity_ModelsAdmin(admin.ModelAdmin):
    list_display =('user_name','activity_name','age_group','fees','duration')
    list_filter =['activity_name','fees']
    search_fields=('activity_name',)    
class AdmissionAdminist(admin.ModelAdmin):
    list_display=('activity_id','parent_user_name','kid_name','age','school_name','standard','mother_name','father_name','phone_no','transaction_id','date') 
    list_filter=['school_name','kid_name'] 
class User_MessageAdmin(admin.ModelAdmin):
    list_display=('receiver_id','sender_id','subject','content','date','receiver_status','sender_status') 
    list_filter=['date'] 
class CityEventAdmin(admin.ModelAdmin):
    list_display=('event_id','event_name','date','city','venue_address','description','pic_name')  
    list_filter=['event_name']
    search_fields=('event_name',)    
admin.site.register(Contact,ContactAdmin)
admin.site.register(CityEvent,CityEventAdmin)
admin.site.register(Organizer, OrganizerAdmin)
admin.site.register(Parent,ParentAdmin)
admin.site.register(Feedback,FeedbackAdmin)
admin.site.register(User_Message, User_MessageAdmin)
admin.site.register(Activity_Models,Activity_ModelsAdmin)

admin.site.site_header="Kidz Planet Admintration"
admin.site.site_title="Kidz Planet Dashboard"
admin.site.index_title="Welcom to the Kidz Planet Admin"

# Register your models here.
