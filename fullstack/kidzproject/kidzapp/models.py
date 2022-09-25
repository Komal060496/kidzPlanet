from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=45,null=False)
    email = models.EmailField(max_length=45,null=False)
    phone = models.CharField(max_length=10,null=False)
    your_query=models.TextField()
    date= models.DateField(default=timezone.now)
    def __str__(self):
        return self.name
class Parent(models.Model):
    user_name= models.CharField(max_length=45,primary_key=True)
    password = models.CharField(max_length=10,null=False)
    name = models.CharField(max_length=45,null=False)
    email = models.EmailField(max_length=45,null=False)
    phone = models.CharField(max_length=10,null=False)
    def __str__(self):
        return self.name
    
class CityEvent(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=100,null=False)
    date= models.DateField(default=timezone.now)
    city = models.CharField(max_length=50,null=False)        
    venue_address = models.TextField(null=False)
    description = models.TextField()
    pic_name= models.ImageField(max_length=255,upload_to="kidzapp/event_pic",default="")
    def __str__(self):
        return self.event_name
class Organizer(models.Model):
    user_name = models.CharField(max_length=45,primary_key=True)
    password = models.CharField(max_length=100,null=False)
    name = models.CharField(max_length=45,null=False)
    email = models.EmailField(max_length=45,null=False) 
    phone = models.CharField(max_length=10,null=False) 
    city = models.CharField(max_length=45,null=False)
    address = models.TextField()
    pic_name = models.FileField(max_length=100,upload_to="kidzapp/picture",default="")  
    def __str__(self):
        return self.name
    
class User_Message(models.Model):
    receiver_id=models.CharField(max_length=45,null=False,default=None) 
    sender_id=models.CharField(max_length=45,null=False,default=None)
    subject=models.CharField(max_length=100,null=False)
    content=models.TextField(null=False)
    date= models.DateField(default=timezone.now)
    receiver_status=models.BooleanField(default=True,null=True)
    sender_status=models.BooleanField(default=True,null=True)
      
class Feedback(models.Model):
    user_name = models.ForeignKey(Parent,null=False,on_delete=models.DO_NOTHING)
    organization_name= models.CharField(max_length=45,null=False)
    feedback_text = models.TextField()
    rating= models.IntegerField()
    date= models.DateField(default=timezone.now)
    
class Activity_Models(models.Model):
     user_name=models.ForeignKey("Organizer",on_delete=models.DO_NOTHING)   
     activity_name=models.CharField(max_length=45,null=False)
     age_group=models.CharField(max_length=45,null=False)
     fees=models.CharField(max_length=45,null=False)
     duration=models.CharField(max_length=45,null=False)

class Admission(models.Model):
    activity_id=models.IntegerField()
    parent_user_name=models.ForeignKey("Parent",on_delete=models.DO_NOTHING)
    kid_name= models.CharField(max_length=45,null=False)
    age=models.CharField(max_length=45,null=False)
    school_name=models.CharField(max_length=100,null=False)
    standard = models.CharField(max_length=45,null=False) 
    mother_name=models.CharField(max_length=45,null=False) 
    father_name=models.CharField(max_length=45,null=False)
    phone_no=models.IntegerField(max_length=10,null=False)
    transaction_id=models.CharField(max_length=45,null=False)
    date= models.DateField(default=timezone.now) 
class Prediction(models.Model):
    name = models.CharField(max_length=45,null=False)
    email = models.EmailField(max_length=45,null=False) 
    age = models.CharField(max_length=100,null=False)
    gender = models.PositiveIntegerField(max_length=1,null=False)
    interest = models.CharField(max_length=100,null=False)
    playgroup = models.PositiveIntegerField(max_length=1,null=False)
    