from django.shortcuts import render, redirect,HttpResponse
from .models import NeedBlood, DonateBlood, GotBlood
from django.contrib.auth import authenticate , login ,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import Http404 ,HttpResponseForbidden
from django.core.mail import BadHeaderError
from django.core.mail import send_mail

def home(request):
    return render(request , 'home.html')


def donater(request):
    x = DonateBlood.objects.all()
    context = {'AllBloodDonater': x}
    return render(request , 'donater.html', context)


def reciever(request):
    allReciever = GotBlood.objects.all()
    context = {"BloodReciever": allReciever}
    return render(request, 'reciever.html',context)


def donate(request):
    BloodNeedperson = NeedBlood.objects.all()
    BloodNeedperson2 = NeedBlood.objects.values('id')
    context = {'AllBloodNeedPerson': BloodNeedperson, 'user_id':BloodNeedperson2}
    return render(request , 'donate.html',context)


def donateform(request,my_id):
    try:
        allBloodNeedPerson = NeedBlood.objects.get(id= my_id)
    except:
        raise Http404
    context = {'personName': allBloodNeedPerson}

    if(request.method=='POST'):
        name= request.POST.get('name')
        email= request.POST.get('email')
        mobile_number= request.POST.get('mobileNumber')
        age= request.POST.get('age')
        address= request.POST.get('address')
        gender= request.POST.get('gender')
        bloodGroup= request.POST.get('bloodGroup')

        donate_blood= DonateBlood.objects.create(person_name= name,person_email= email,person_mobileNumber=mobile_number,
                              person_age = age, person_address= address, 
                              person_gender = gender, person_bloodGroup= bloodGroup)
        got_blood= GotBlood.objects.create(person_name= allBloodNeedPerson.person_name,
                                                   person_email= allBloodNeedPerson.person_email,
                                                   person_mobileNumber=allBloodNeedPerson.person_mobileNumber,
                                                    person_age = allBloodNeedPerson.person_age, 
                                                    person_address= allBloodNeedPerson.person_address, 
                                                    person_gender = allBloodNeedPerson.person_gender, 
                                                    person_bloodGroup= allBloodNeedPerson.person_bloodGroup,
                                                    person_reason= allBloodNeedPerson.person_reason)
 
        # send_mail(
        #     'Blood Bank',
        #     'Your form have been submitted succssfully! \n Thanks for support Neddy People',
        #     'anilsainisukhpura@gmail.com',
        #     [email],
        #     fail_silently=False,
        #      )
        # send_mail(
        #     'Blood Bank',
        #      "Congratulation someone is ready to give you blood",
        #     'anilsainisukhpura@gmail.com',
        #     [allBloodNeedPerson.person_email],
        #     fail_silently=False,
        #      )
        allBloodNeedPerson.delete()
        
        messages.success(request, "Your Form Has Been Submmited")
    return render(request , 'donateform.html',context)

def needBlood(request):
    if(request.method=='POST'):
        name= request.POST.get('name')
        email= request.POST.get('email')
        mobile_number= request.POST.get('mobileNumber')
        age= request.POST.get('age')
        reason= request.POST.get('reason')
        address= request.POST.get('address')
        gender= request.POST.get('gender')
        bloodGroup= request.POST.get('bloodGroup')

        need_blood= NeedBlood.objects.create(user=request.user,person_name= name,person_email= email,person_mobileNumber=mobile_number,
                              person_age = age, person_reason= reason, person_address= address, 
                             person_gender = gender, person_bloodGroup= bloodGroup)
        need_blood.save()

        # send_mail(
        #     'Blood Bank',
        #     'Your Blood Request has been submited! We hope you will get blood soon',
        #     'anilsainisukhpura@gmail.com',
        #     [email],
        #     fail_silently=False,
        #      )

        messages.success(request, "Your Form Has Been Submmited succesfully")

    return render(request , 'needBlood.html')
    


def aboutUs(request):
    return render(request , 'aboutUs.html')

def handleSignUp(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if(password1!=password2):
            messages.error(request, "password should be match")
            return  redirect('home')
        if(len(username)<3 or len(username)>11):
            messages.error(request ,"username under 4 to 10")
            return redirect('home')
        
        myUser = User.objects.create_user(username, email ,password1)
        myUser.save()
        messages.success(request, 'You Are login successfully')
        return redirect('home')
    else:
        return render(request , 'signup.html')

def handleLogin(request):
    if request.method =="POST":

        loginusername = request.POST['username']
        loginpassword = request.POST['password']

        user = authenticate(username =loginusername, 
               password = loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"login successfully")
            return redirect('home')
        else:
            messages.error(request,"try again")
            return redirect('handleLogin')
    return render(request , 'login.html')

def handleLogout(request):
    logout(request)
    messages.success(request,"logout successfully")
    return redirect('home')
    
def persondetails(request,my_id):
    try:
        allBloodNeedPerson = NeedBlood.objects.get(id= my_id)
    except:
        raise Http404

    context = {'personName': allBloodNeedPerson}
    if request.method=='POST':
        allBloodNeedPerson = NeedBlood.objects.get(id= my_id)
        if request.user != allBloodNeedPerson.user:
            raise HttpResponseForbidden
        allBloodNeedPerson.delete()
        return redirect('donate')
        messages.success(request,"post is deleted successfully")

    return render(request,'personDetails.html', context)