from django.shortcuts import render,redirect
from django.db.models import Q
from ormApp.forms import EmployeeForm
from django.db.models import Min,Max,Avg,Sum,Count
from ormApp.models import Employee

# Create your views here.
def index_view(request):
    return render(request,'ormApp/index.html')

def home_view(request):
    form = EmployeeForm()
    if request.method=='POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return back_view(request)
    return render(request,'ormApp/home.html',{'form':form})

def back_view(request):
    list = Employee.objects.all()
    return render(request,'ormApp/back.html',{'list':list})

def delete_view(request,id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect('/')

def update_view(request,id):
    employee = Employee.objects.get(id=id)
    if request.method=='POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/back')
    return render(request,'ormApp/update.html',{'employee':employee})

def display_view(request):
    avg1 = Employee.objects.all().aggregate(Avg('salary'))
    min1 = Employee.objects.all().aggregate(Min('salary'))
    max1 = Employee.objects.all().aggregate(Max('salary'))
    sum1 = Employee.objects.all().aggregate(Sum('salary'))
    count1 = Employee.objects.all().aggregate(Count('salary'))
    return render(request,'ormApp/aggrigate.html',{'avg1':avg1,'min1':min1,'max1':max1,'sum1':sum1,'count1':count1})



