from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth,User
from .models import Animals
from .models import Worker
from .models import *


# def booking(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         food = request.POST.get('food')
#
#         Animals.objects.create(name=name,food=food)
#
#         return redirect('')
#
#     else:
#         return render(request,'booking.html')


def animal_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        food = request.POST.get('food')

        Animals.objects.create(name=name,food=food)

        return redirect('')

    else:
        return render(request,'animal.html')

import sys
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # user = auth.authenticate(username = username, password = password)

        if Worker.objects.filter(username=username, password=password).exists():
                uid = Worker.objects.get(username=username)
                request.session['username'] = username
                request.session['worker_id'] = uid.id
                print("Loggin")
                # sys.exit();
                return redirect('/')
        # if user is not None:
        #     auth.login(request,user)
        #     return redirect('register')
        else:
            print("User not exist")
            messages.warning(request,"Invalid Password!")
            return redirect('login')


    else:
        return render(request,'login.html')




def register(request):

    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        nid = request.POST['nid']
        upload_nid = request.POST['upload_nid']
        pic = request.POST['pic']
        phone = request.POST['phone']
        address = request.POST['address']
        location = request.POST['location']
        type_of_work = request.POST['type_of_work']

        if password1 == password2:
            if Worker.objects.filter(username=username).exists():
                messages.warning(request,"Username has been taken previously!")
                return redirect('register')
            elif Worker.objects.filter(email=email).exists():
                  messages.warning(request,"Email has been taken previously!")
                  return redirect('register')
            elif Worker.objects.filter(nid=nid).exists():
                  messages.warning(request,"NID has been taken previously!")
                  return redirect('register')
            else:

                worker = Worker.objects.create(name=name, username=username, email=email, password=password1, nid=nid, upload_nid=upload_nid, pic=pic,
                                        phone=phone, address=address, location=location, type_of_work=type_of_work)
                worker.save()
                messages.success(request,"Registration Succussful!")
                return redirect('login')
        else:
            messages.warning(request,"Password not match!")
            return redirect('register')




    else:

        return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
