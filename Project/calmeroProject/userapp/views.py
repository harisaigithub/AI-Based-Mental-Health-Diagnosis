from django.shortcuts import render,redirect
from django.contrib import messages
import urllib.request
import urllib.parse
from django.contrib.auth import logout
from django.core.mail import send_mail
import os
import random
from django.conf import settings
from userapp.models import *
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from io import BytesIO
from django.http import HttpResponse
from PIL import Image
import base64
from django.utils.datastructures import MultiValueDictKeyError
import time


def user_logout(request):
    logout(request)
    messages.info(request, "Logout Successfully ")
    return redirect("login")

EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')



def generate_otp(length=4):
    otp = "".join(random.choices("0123456789", k=length))
    return otp




def index(request):
    return render(request,"index.html")



def our_services(request):
    return render(request,"services.html")



def contact(request):
    return render(request,"contact.html")





def about(request):
    return render(request,"about.html")




def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        try:
            user = User.objects.get(email=email)
            if user.password != password:
                messages.error(request, "Incorrect password.")
                return redirect("login")
            if 12 == 12:
                if user.otp_status == "Verified":
                    request.session["user_id_after_login"] = user.pk
                    messages.success(request, "Login successful!")
                    return redirect("user_dashboard")
                else:
                    new_otp = generate_otp()
                    user.otp = new_otp
                    user.otp_status = "Not Verified"
                    user.save()
                    subject = "New OTP for Verification"
                    message = f"Your new OTP for verification is: {new_otp}"
                    from_email = settings.EMAIL_HOST_USER
                    recipient_list = [user.email]
                    send_mail(
                        subject, message, from_email, recipient_list, fail_silently=False
                    )
                    request.session["id_for_otp_verification_user"] = user.pk
                    return redirect("user_otp")
            else:
                messages.info(request, "Your Account is Not Accepted by Admin Yet")
                return redirect("login")
        except User.DoesNotExist:
            messages.error(request, "No User Found.")
            return redirect("login")
    return render(request,"login.html")





def user_register(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password') 
        phone_number = request.POST.get('phone_number')
        age = request.POST.get('age')
        address = request.POST.get('address')
        photo = request.FILES.get('photo')
        if User.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists.")
            return redirect('user_register') 
        user = User(
            full_name=full_name,
            email=email,
            password=password, 
            phone_number=phone_number,
            age=age,
            address=address,
            photo=photo
        )
        otp = generate_otp()
        user.otp = otp
        user.save()
        subject = "OTP Verification for Account Activation"
        message = f"Hello {full_name},\n\nYour OTP for account activation is: {otp}\n\nIf you did not request this OTP, please ignore this email."
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        request.session["id_for_otp_verification_user"] = user.pk
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        messages.success(request, "Otp is sent your mail and phonenumber !")
        return redirect("user_otp")
    return render(request,"user-register.html")





def user_otp(request):
    otp_user_id = request.session.get("id_for_otp_verification_user")
    if not otp_user_id:
        messages.error(request, "No OTP session found. Please try again.")
        return redirect("user_register")
    if request.method == "POST":
        entered_otp = "".join(
            [
                request.POST["first"],
                request.POST["second"],
                request.POST["third"],
                request.POST["fourth"],
            ]
        )
        try:
            user = User.objects.get(id=otp_user_id)
        except User.DoesNotExist:
            messages.error(request, "User not found. Please try again.")
            return redirect("user_register")
        if user.otp == entered_otp:
            user.otp_status = "Verified"
            user.save()
            messages.success(request, "OTP verification successful!")
            return redirect("login")
        else:
            messages.error(request, "Incorrect OTP. Please try again.")
            return redirect("user_otp")
    return render(request,"user-otp.html")



def user_dashboard(request):
    return render(request,"user-dashboard.html")



def chatbot(request):
    return render(request,"chatbot.html")





def user_profile(request):
    user_id = request.session.get('user_id_after_login')
    print(user_id)
    user = User.objects.get(pk=user_id)
    
    if request.method == "POST":
        # Get values from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        location = request.POST.get('location')

        # Update only if the value is not empty
        if name:
            user.full_name = name
        if email:
            user.email = email
        if phone:
            user.phone_number = phone
        if password:
            user.password = password
        if location:
            user.address = location
        
        # Handle profile image upload (only update if a new image is provided)
        try:
            profile = request.FILES['profile']
            user.photo = profile
        except MultiValueDictKeyError:
            # If no new profile is provided, keep the existing one
            pass

        # Save the user object with the updated fields
        user.save()
        messages.success(request, 'Updated successfully!')
        return redirect('user_profile')

    return render(request, 'user-profile.html', {'user': user})






def user_feedback(request):
    user_id = request.session.get('user_id_after_login')
    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        rating = int(request.POST.get('rating'))
        additional_comments = request.POST.get('additional_comments')
        UserFeedback.objects.create(
            user=user,
            rating=rating,
            additional_comments=additional_comments
        )
        messages.success(request, 'Feedback submitted successfully.')
        return redirect('user_feedback')
    return render(request,"user-feedback.html",{'user':user})
