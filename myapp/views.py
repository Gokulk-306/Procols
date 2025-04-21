from django.shortcuts import render, redirect
from django.core.mail import send_mail
from.models import StudentCallList
from django.contrib import messages


def register(request):
    return render(request, 'register.html')

def contact(request):
    return render(request, 'reviews.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        Your_Name = request.POST.get('Your_Name')
        Email = request.POST.get('Email')
        Mobile_No = request.POST.get('Mobile_No')
        City = request.POST.get('City')
        College_Name = request.POST.get('College_Name')  # Fixed typo here
        Department = request.POST.get('Department')

        StudentCallList.objects.create(
            Your_Name=Your_Name,
            Email=Email,
            Mobile_No=Mobile_No,
            City=City,
            College_Name=College_Name,
            Department=Department
        )

        subject = 'New Student Details'
        message = f'A new student has registered:\n\nName:{Your_Name} \n\nEmail:{Email} \n\nMobile No: {Mobile_No} \n\nCity: {City} \n\nCollege Name: {College_Name} \n\nDepartment: {Department}'
        from_email='connect.procols@gmail.com'
        to_email=['connect.procols@gmail.com']

        send_mail(subject, message, from_email, to_email)
        messages.success(request, 'Thank you! Your consultasion has been submitted successfully.')
        return redirect('index')
    return render(request, 'register.html')


