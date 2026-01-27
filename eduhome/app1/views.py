from django.shortcuts import render
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
    return render(request, 'contact.html')

