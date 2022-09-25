from django.urls import path
from  .import views
from  .import organizer_views,message_views

urlpatterns = [
   path("",views.home,name="home"),
   path("aboutus/",views.aboutus,name="aboutus"),
   
   path("contactus/",views.contactus,name="contactus"),
   path("parent_reg/",views.parent_reg,name="parent_reg"),
   path("login/",views.login,name="login"),
   path("parent_logout/",views.parent_logout,name="parent_logout"),
   path("parent_editProfile/",views.parent_editProfile,name="parent_editProfile"),
   path("organizer_reg/",organizer_views.organizer_reg,name="organizer_reg"),
   path("org_login/",organizer_views.org_login,name="org_login"),
   path("org_logout/",organizer_views.org_logout,name="org_logout"),
   path("view_feedback/",organizer_views.View_Feedback.as_view(),name="view_feedback"),
   path("upload_pic/",organizer_views.upload_pic,name="upload_pic"),
   path("org_editProfile/",organizer_views.org_editProfile,name="org_editProfile"),
   path("courses/",views.courses,name="courses"),
   path("trail/",views.trail,name="trail"),
   path("view_act/",views.view_act,name="view_act"),
   path("compose_message/",message_views.Compose_Message.as_view(),name="compose_message"),
   path("user_inbox/",message_views.User_Inbox.as_view(),name="user_inbox"),
   path("delete_message/",message_views.Delete_Message.as_view(),name="delete_message"),
   path("show_message/<int:msg_id>",message_views.Show_Message.as_view(),name="show_message"),
   path("show_activity/<str:username>",views.Show_Activity.as_view(),name="show_activity"),
   path("feed_back/<str:username>",views.Feed_back.as_view(),name="feed_back"),
   path("enrollment_form/<int:p_id>",views.Enrollment_Form.as_view(),name="enrollment_form"),
   path("add_activity/",organizer_views.Add_Activity.as_view(),name="add_activity"),
   path("final_admission/",views.final_admission,name="final_admission"),
   path("final_feedback/",views.final_feedback,name="final_feedback"),
   path("validate_username/",views.validate_username,name="validate_username"),
   path("validate_username1/",organizer_views.validate_username1,name="validate_username1"),
   path("common_feedback/",views.common_feedback,name="common_feedback"),
   path("search/",views.search,name="search"),
   path("predict/",views.Predict.as_view(),name="predict"),
   path("back/<str:id>/",views.back.as_view(),name="back"),
]
