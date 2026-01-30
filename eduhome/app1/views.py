from django.http import HttpResponse
from django.shortcuts import render
from app1.models import Contact
from app1.models import signup
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
def course(request):
    return render(request, 'course.html')   
def course_details(request):
    return render(request, 'course-details.html')
def event(request):
    return render(request, 'event.html')
def event_details(request):
    return render(request, 'event-details.html')
def teacher(request):
    return render(request, 'teacher.html')
def teacher_details(request):
    return render(request, 'teacher-details.html')
def blog(request):
    return render(request, 'blog.html')
def blog_details(request):
    return render(request, 'blog-details.html')    
#contact form data handling in sqlite database   
def contact(request):
    if request.method == 'POST':
        con_name = request.POST.get('con_name')
        con_email = request.POST.get('con_email')
        con_subject = request.POST.get('con_subject')
        con_message = request.POST.get  ('con_message')
        contact = Contact.objects.create(con_name=con_name, con_email=con_email, con_subject=con_subject, con_message=con_message)
        return HttpResponse('Your message has been sent successfully. Thank you for contacting us.')
    return render(request, 'contact.html')

# Signup form handling and user creation
def signup(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return HttpResponse("Passwords do not match. Please try again.")
        else:
            user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username,  email=email, password=password)
            user.save()
        return redirect('/userlogin/')
    return render(request, 'signup.html')

# User login handling authentication 
def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/blog/' )  # Redirect to home page after successful login
        else:
            return HttpResponse("Invalid credentials. Please try again.")
    return render(request, 'userlogin.html')


                                             

