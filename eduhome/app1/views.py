from django.http import HttpResponse
from django.shortcuts import render
from app1.models import Contact
# Create your views here.

def index(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')
def signup(request):
    return render(request, 'signup.html')
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


def contact(request):
    if request.method == 'POST':
        con_name = request.POST.get('con_name')
        con_email = request.POST.get('con_email')
        con_subject = request.POST.get('con_subject')
        con_message = request.POST.get  ('con_message')
        contact = Contact.objects.create(con_name=con_name, con_email=con_email, con_subject=con_subject, con_message=con_message)
        return HttpResponse('Your message has been sent successfully. Thank you for contacting us.')
    return render(request, 'contact.html')


                                             

