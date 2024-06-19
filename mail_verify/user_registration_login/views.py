from django.http import HttpResponse
from django.shortcuts import render, redirect
from random import randint
import smtplib
import ssl
from email.message import EmailMessage
from .models import User_Login_Data

def Register(request):
    return render(request, "index.html")

def verify(request):
    if request.method=='POST':
        usermail=request.POST.get('email')

        email_sender = "contactcode.ag@gmail.com"
        email_pwd = "jjeb gqfz sdrp osxo"
        global otp
        otp = randint(100000,1000000)


        subject = "OTP Verification"
        body = " Your otp for verification is: " + str(otp)
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = usermail
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
            smtp.login(email_sender, email_pwd)
            smtp.sendmail(email_sender, usermail, em.as_string())
        return render(request, 'verify.html')     
 

    else :
        return redirect("Register")


def submit(request):
    if request.method=='POST':
        otp_recv=request.POST.get('otp')
     
        if otp_recv == otp:
            name = request.POST.get('name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            
     
            # Save the data to the database
            User_Login_Data.objects.create(name=name, username=username, email=email, password=password)
            return redirect('login')
        else:
            return redirect('Register')
            print("Hagdiya")

    else:
        return redirect("Register")
        print("else was exe")



def login(request):
    return render(request,'login.html')
