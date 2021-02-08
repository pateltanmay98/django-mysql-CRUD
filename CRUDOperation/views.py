from django.shortcuts import render, redirect

from .forms import EmployeeForm
from .models import Employee


# Create your views here.

def welcome(request):
    return render(request, "welcome.html", context=None)


def load_form(request):
    form = EmployeeForm
    return render(request, 'index.html', {'form': form})


def add(request):
    form = EmployeeForm(request.POST)
    form.save()
    return redirect('/show')


def show(request):
    employee = Employee.objects.all
    return render(request, 'show.html', {'employee': employee})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    form.save()
    return redirect('/show')


def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')


def search(request):
    get_name = request.POST['name']
    employee = Employee.objects.filter(ename=get_name)
    return render(request, 'show.html', {'employee': employee})
