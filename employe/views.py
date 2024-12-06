from django.shortcuts import render,  reverse
from django.shortcuts import HttpResponse

from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

from common.decorators import allow_employee
from employe.models import *
from managers.models import *
from users.models import *


@login_required(login_url='/login')
@allow_employee
def details(request):
    user = request.user
    employe = Employe.objects.get(user=user)
    contact = EmergencyContact.objects.get(employe=employe)
    address = Address.objects.get(employe=employe)
    background = Background.objects.get(employe=employe)
    benefits = Benefits.objects.get(employe=employe)
    identification = Identification.objects.get(employe=employe)
    shedule = WorkSchedule.objects.get(employe=employe)
    holidays = Holiday.objects.all()

    context ={
        'employe': employe,
        'user': user,
        'contact': contact,
        'address': address,
        'background': background,
        'benefits': benefits,
        'identification': identification,
        'schedule': shedule,
        'holidays':holidays
    }

    return render(request, "employe/details.html", context=context)


@login_required(login_url='/login')
@allow_employee
def leaveform(request):
    
    user = request.user
    employe = Employe.objects.get(user=user)

    if request.method =='POST':
        subject = request.POST.get('subject')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        leave_type = request.POST.get('leave_type')
        description = request.POST.get('description')
        file = request.FILES.get('file')

        leaveform = LeaveReaquest.objects.create(
            subject=subject,
            leave_type=leave_type,
            description= description,
            file = file,
            employe=employe,
            start_date = start_date,
            end_date = end_date
        )
        leaveform.save()
        return HttpResponseRedirect(reverse("employe:details"))
    return render(request, "employe/leaveform.html")


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("employe:login"))


def login(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        employe_id = request.POST.get("employe_id")


        if email and password:
            user = authenticate(request, email=email, password=password,employe_id=employe_id)
            if user is not None:
                auth_login(request, user)

                return HttpResponseRedirect(reverse("employe:details"))
            
            else:
                context ={
                    "title":"Login",
                    "error":True,
                    "message":"invalid credentials"
                }

            return render(request, "employe/login.html", context=context)
        else:
            context ={
                "title":"Login",
                "error":True,
                "message":"invalid credentials"
            }
            return render(request, "employe/login.html", context=context)
            
    else:
        context ={
            "title":"Login",
        }
        return render(request, "employe/login.html", context=context)


@login_required(login_url='/login')
@allow_employee
def leavelist(request):
    instances = LeaveReaquest.objects.all()

    # Calculate leave duration for each instance
    for instance in instances:
        instance.leave_duration = (instance.end_date - instance.start_date).days + 1
    
    return render(request, "employe/leavelist.html", {'instances': instances})




@login_required(login_url='/login')
@allow_employee
def viewlist(request, id):
    
    leave_request = LeaveReaquest.objects.get(id=id)
    employee = leave_request.employe
    user = employee.user 
    
    return render(request, 'employe/viewlist.html', {
        'user': user,
        'employe': employee,
        'leave_request': leave_request,
    })



@login_required(login_url='/login')
@allow_employee
def edit_employe(request, id):
    employe = Employe.objects.get(id=id)
    user = employe.user
    contact = EmergencyContact.objects.get(employe=employe)
    address = Address.objects.get(employe=employe)
    background = Background.objects.get(employe=employe)
    benefits = Benefits.objects.get(employe=employe)
    identification = Identification.objects.get(employe=employe)
    schedule = WorkSchedule.objects.get(employe=employe)

    user_date_of_birth = employe.user.date_of_birth.strftime('%Y-%m-%d') if employe.user.date_of_birth else ''

    date_joining = employe.date_of_joining.strftime('%Y-%m-%d') if employe.date_of_joining else ''

    # Format the time fields
    schedule_start_time = schedule.start_time.strftime('%H:%M') if schedule.start_time else ''
    schedule_end_time = schedule.end_time.strftime('%H:%M') if schedule.end_time else ''

    if request.method == 'POST':
        # User details
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.employe_id = request.POST.get('employe_id')
        user.phone_number = request.POST.get('phone_number')
        user.date_of_birth = request.POST.get('date_of_birth')
        user.gender = request.POST.get('gender')
        user.maritul_status = request.POST.get('maritul_status')
        user.save()

        # Emergency Contact
        contact.contact_name = request.POST.get('contact_name')
        contact.contact_number = request.POST.get('contact_number')
        contact.relationship = request.POST.get('relationship')
        contact.country = request.POST.get('emergency_country')
        contact.city = request.POST.get('emergency_city')
        contact.pincode = request.POST.get('emergency_pincode')
        contact.save()

        # Employee details
        employe.department = request.POST.get('department')
        employe.designation = request.POST.get('designation')
        employe.date_of_joining = request.POST.get('date_of_joining')
        employe.employment_Type = request.POST.get('employment_Type')
        employe.reporting_manager = request.POST.get('reporting_manager')
        employe.work_location = request.POST.get('work_location')
        employe.employe_status = request.POST.get('employe_status')
        employe.save()

        # Address
        address.permanent_address = request.POST.get('permanent_address')
        address.country = request.POST.get('country')
        address.city = request.POST.get('city')
        address.pincode = request.POST.get('pincode')
        address.save()

        # Benefits
        benefits.salary_details = request.POST.get('salary_details')
        benefits.bank_name = request.POST.get('bank_name')
        benefits.account_number = request.POST.get('account_number')
        benefits.branch_name = request.POST.get('branch_name')
        benefits.ifsc_code = request.POST.get('ifsc_code')
        benefits.pancard = request.POST.get('pancard')
        benefits.pf_fund = request.POST.get('pf_fund')
        benefits.state_insurance_number = request.POST.get('state_insurance_number')
        benefits.save()

        # Background
        background.educational_qualifications = request.POST.get('educational_qualifications')
        background.previous_details = request.POST.get('previous_details')
        background.save()

        # Identification
        identification.work_authorization = request.POST.get('work_authorization')
        identification.save()

        # Work Schedule
        schedule.start_time = request.POST.get('start_time')
        schedule.end_time = request.POST.get('end_time')
        schedule.save()

        return HttpResponseRedirect(reverse("employe:detail"))

    context = {
        'employe': employe,
        'user': user,
        'contact': contact,
        'address': address,
        'background': background,
        'benefits': benefits,
        'identification': identification,
        'schedule': schedule,
        'user_date_of_birth': user_date_of_birth,
        'schedule_start_time': schedule_start_time,
        'schedule_end_time': schedule_end_time,
        'date_joining': date_joining
    }

    return render(request, "employe/edit_employe.html", context=context)