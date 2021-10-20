from django.shortcuts import render, redirect
from application.models import Employee
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import re
from datetime import datetime


EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")


# Display employee list function.
def Employee_List(request):
    Qry_All_Employee = Employee.objects.all()
    context = {
        'Employee_List':Qry_All_Employee
    }
    return render(request, 'Employee_List.html', context)


# Add employees function.
def Add_Employee(request):
    if request.method == 'GET':
        return render(request, 'Add_Employee.html')
    else:
        Image = request.FILES['image']
        error = False

        if len(request.POST['firstname']) < 2:
            messages.error(request, "FirstName must be 2 or more characters !")
            error = True

        elif (len(request.POST['lastname']) < 2):
            messages.error(request, "LastName must be 2 or more characters !")
            error = True

        elif (Employee.objects.filter(email=request.POST['email']).exists()):
            messages.error(request, "Email Address is already taken !")
            error = True

        elif not (EMAIL_REGEX.match(request.POST['email'])):
            messages.error(request, "Email is invalid !")
            error = True

        elif (Image.size > 6000000):
            messages.error(request, 'Image Size Must Less-than 5mb.')
            error = True

        if (error):
            return redirect('/Add_Employee')
        else:
            Qry_Add_Employee = Employee(firstname=request.POST['firstname'],
                                        lastname=request.POST['lastname'],
                                        email=request.POST['email'],
                                        salary=request.POST['salary'],
                                        image=Image.name)
            Qry_Add_Employee.save()
            
            # Photo save a Profile_Photos in media directory
            FS = FileSystemStorage('./media/employee_image/')
            FS.save(Image.name, Image)
            
            return redirect('/')


# Update employees function.
def Update_Employee(request, id):
    if request.method == 'GET':
        Qry_Edit_Employee = Employee.objects.get(id=id)
        context = {
            'Employee': Qry_Edit_Employee,
        }
        return render(request, 'Update_Employee.html', context)
    else:
        try:
            Image = request.FILES['image']
        except:
            Image = ''

        if Image:
            Qry_Edit_Employee = Employee.objects.get(id=id)
            Qry_Edit_Employee.image = Image.name
            Qry_Edit_Employee.updated_date = datetime.now()
            Qry_Edit_Employee.save()
            
            # Photo save a Profile_Photos in media directory
            FS = FileSystemStorage('./media/employee_image/')
            FS.save(Image.name, Image)
            
            return redirect('/')
        else:
            error = False
            if len(request.POST['firstname']) < 2:
                messages.error(request, "FirstName must be 2 or more characters !")
                error = True

            elif (len(request.POST['lastname']) < 2):
                messages.error(request, "LastName must be 2 or more characters !")
                error = True

            elif not (EMAIL_REGEX.match(request.POST['email'])):
                messages.error(request, "Email is invalid !")
                error = True

            if (error):
                return redirect('/Add_Employee')
            else:
                Qry_Edit_Employee = Employee.objects.get(id=id)
                Qry_Edit_Employee.firstname = request.POST['firstname']
                Qry_Edit_Employee.lastname = request.POST['lastname']
                Qry_Edit_Employee.email = request.POST['email']
                Qry_Edit_Employee.salary = request.POST['salary']
                Qry_Edit_Employee.updated_date = datetime.now()
                Qry_Edit_Employee.save()
                return redirect('/')


# Delete employees function.
def Delete_Employee(request, id):
    Qry_Delete_Employee = Employee.objects.get(id=id)
    Qry_Delete_Employee.delete()
    return redirect('/')


# List of employees those employee have same salary function.
def Same_Salary(request):
    # Qry_All_Employee = Employee.objects.all()
    Qry_All_Employee = Employee.objects.raw("""
        SELECT *
        FROM Employee e
        INNER JOIN
        (
           SELECT salary
           FROM Employee
           GROUP BY salary
           HAVING COUNT(*) > 1
        ) grp ON e.salary = grp.salary
        ORDER BY salary;
    """)
    context = {
        'Employee_List':Qry_All_Employee
    }
    return render(request, 'Same_Salary.html', context)


# List of employees those employee have second lowest salary function.
def Second_Lowest_Salary(request):
    Qry_All_Employee = Employee.objects.all().order_by('salary')[1:2]
    context = {
        'Employee_List':Qry_All_Employee
    }
    return render(request, 'Second_Lowest_Salary.html', context)


# Top 10 salary of employee function.
def Top_10_Salary(request):
    Qry_All_Employee = Employee.objects.all().order_by('-salary')[:10]
    context = {
        'Employee_List':Qry_All_Employee
    }
    return render(request, 'Top_10_Salary.html', context)
