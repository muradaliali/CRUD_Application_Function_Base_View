from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegisration
from .models import user
#this function with Add new student and show all datat from datatbase
def add_show(request):
    if request.method =='POST':
        fm = StudentRegisration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = user(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegisration()
    else:
        fm = StudentRegisration()
    stud = user.objects.all()
    return render(request,'enroll/addandshow.html',{'form': fm, 'stu': stud})
#this function will delete
def delete(request,id):
    if request.method =='POST':
        pi = user.objects.get(pk = id)
        pi.delete()
        return HttpResponseRedirect("/")
#this function will update data
def update(request,id):
    if request.method =='POST':
        pi = user.objects.get(pk=id)
        fm = StudentRegisration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = user.objects.get(pk=id)
        fm = StudentRegisration( instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':fm})
# this functions use for documentation