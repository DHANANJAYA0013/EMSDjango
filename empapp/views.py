from django.shortcuts import render,HttpResponse,redirect
from .models import Employee,Department,Position
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')



def filter(request):
    if request.method=='POST':
       name=request.POST["name"]
       dept=request.POST["department"]
       pos=request.POST["position"] 
       emps=Employee.objects.all()
       if name:
           emps=emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
       if dept:
           emps=emps.filter(department__name__icontains = dept)
       if pos:
           emps=emps.filter(position__title__icontains = pos)

       context={
            'emp': emps
        }
       return render(request, 'view_emp.html', context)
    elif request.method=="GET":
        return render(request, 'filter.html')
    else:
        return HttpResponse("An Exception occured ! an employee has not been added.")

       



def view(request):
    emps=Employee.objects.all()
    context = {
        'emp': emps
    }
    return render(request, 'view_emp.html',context)


def add(request):
    if request.method == 'POST':
        # Handle the POST request logic as before
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        salary = request.POST["salary"]
        phone_number = request.POST["phone_number"]
        gender = request.POST["gender"]
        date_of_birth = request.POST["date_of_birth"]
        date_of_hire = request.POST["date_of_hire"]
        
        # Get department and position from the dropdown
        department_id = request.POST["department"]
        position_id = request.POST["position"]
        
        # Fetch department and position objects from the DB
        department = Department.objects.get(id=department_id)
        position = Position.objects.get(id=position_id)
        
        # Save the new employee to the DB
        new_employee = Employee(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            gender=gender,
            date_of_birth=date_of_birth,
            date_of_hire=date_of_hire,
            department=department,
            position=position,
            salary=salary
        )
        new_employee.save()

        # Redirect to another page or render success message
        return redirect('view')
    
    else:
        # If it's a GET request, send departments and positions to the template
        departments = Department.objects.all()
        positions = Position.objects.all()

        return render(request, 'add_emp.html', {
            'departments': departments,
            'positions': positions,
        })

    
def remove(request, e_id= 0):
    if e_id:
        try:
            emp_to_removed=Employee.objects.get(id=e_id)
            emp_to_removed.delete()
            return redirect('view')
        except:
            return HttpResponse("Enter valid id.")
    emps=Employee.objects.all()
    context = {
        'emp': emps
    }
    return render(request, 'remove_emp.html',context)