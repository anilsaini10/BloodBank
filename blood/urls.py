from .import views
from django.urls import path, include


urlpatterns = [
    path("",views.home,name= 'home'),
    path('donate/',views.donate,name= 'donate'),
    path('donateform/<int:my_id>/',views.donateform,name= 'donateform'),
    path('persondetails/<int:my_id>',views.persondetails,name= 'persondetails'),
    path('needBlood/',views.needBlood,name= 'needBlood'),
    path('donater/',views.donater,name= 'donater'),
    path('reciever/',views.reciever,name= 'reciever'),
    path('aboutUs/',views.aboutUs,name= 'aboutUs'),
    path('handleLogin/',views.handleLogin,name= 'handleLogin'),
    path('handleSignUp/',views.handleSignUp,name= 'handleSignUp'),
    path('handleLogout/',views.handleLogout,name= 'handleLogout'),
]