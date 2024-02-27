from django.shortcuts import render,redirect
from studentapp.models import Student_Notification,Student,Student_Feedback,Student_Leave
from django.contrib import messages


def Home(request):
    return render(request,'Student/home.html')

def STUDENT_FEEDBACK(request):
    return render(request,'Student/feedback.html')



def STUDENT_LEAVE(request):
    student = Student.objects.get(admin=request.user.id)
    student_leave_history =Student_Leave.objects.filter(student_id= student)

    context={
        'student_leave_history':student_leave_history,
    }
    return render(request,'Student/apply_leave.html',context)


def STUDENT_LEAVE_SAVE(request):
    if  request.method=='POST':
        leave_date=request.POST.get('leave_date')
        leave_message=request.POST.get('leave_message')
        
        
        student_id= Student.objects.get(admin=request.user.id)

        student_leave =Student_Leave(
            student_id=student_id,
            date=leave_date,
            message=leave_message,

        )
        student_leave.save()
        messages.success(request,"Your Leave Application has been submitted")
        return redirect('student_leave')