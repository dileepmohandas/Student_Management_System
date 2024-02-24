from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from studentapp.models import Course,Session_Year

@login_required(login_url='/')
def Home(request):
    return render(request,'Hod/home.html')


@login_required(login_url='/')
def ADD_STUDENT(request):
    course =  Course.objects.all()
    session_year = Session_Year.objects.all()

    context =  {
        'course':course , 
        'session_year' : session_year,
    }
    
        
    return render(request,'Hod/add_student.html',context)
