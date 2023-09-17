from django.shortcuts import render, redirect
from .models import Employee
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def home(request):
    emp_data = Employee.objects.all()
    return render(request,"index.html",{"emp_data":emp_data})

@login_required(login_url="/login/")
def Search(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if (name != None):
            emp_data = Employee.objects.filter(Name__contains=name)
            return render(request,"index.html",{"emp_data":emp_data})
        else:
            pass
    return redirect("/")

@login_required(login_url="/login/")
def add_employee(request):
    if request.method == 'POST':
        empobj = Employee()
        empobj.Name = request.POST.get('name')
        empobj.Department = request.POST.get('department')
        empobj.Salary = request.POST.get('salary')
        empobj.save()
        return redirect("/")
        
    return render(request,"add_employee.html")

@login_required(login_url="/login/")
def edit_employee(request,emp_id):
    emp_data = Employee.objects.get(emp_id=emp_id)
    if request.method == 'POST':
        emp_data.Name = request.POST.get('name')
        emp_data.Department = request.POST.get('department')
        emp_data.Salary = request.POST.get('salary')
        emp_data.save()
        return redirect("/")
    
    return render(request,"edit_employee.html",{"emp_data":emp_data})

@login_required(login_url="/login/")
def delete_employee(request,emp_id):
    emp_data = Employee.objects.get(emp_id=emp_id)
    if (emp_data):
        emp_data.delete()
        return redirect("/")


def user_login(request):
    if (request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,"Invalid Username.")
            return redirect("/login/")
        
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request,"Invalid Password.")
            return redirect("/login/")
        else:
            login(request,user)
            return redirect("/")

    return render(request,"login.html")

def user_logout(request):
    logout(request)
    return redirect("/login/")

def user_register(request):
    if (request.method == "POST"):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request,"Username already taken.")
            return redirect("/register/")

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )
        user.set_password(password)
        user.save()

        messages.info(request,"Account Created Successfully.")

        return redirect("/register/")
    
    return render(request,"register.html")