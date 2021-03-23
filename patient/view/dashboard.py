from django.shortcuts import render,redirect
from patient.models import Patient
from django.http import JsonResponse

# Create your views here.

def patient_data(request):

        patients = Patient.objects.all()

        patients_list = []

        for patient in patients:
            patient_dict = {
                'id':patient.id,
                'first_name': patient.first_name,
                'last_name': patient.last_name,
                'dob': patient.dob,
            }
            patients_list.append(patient_dict)

        return render(request,'patient_data.html',{'data':patients_list})

def add_patient(request):

        return render(request,'add_patient.html')

def submit_data(request):
    if request.POST:
        patient_obj = Patient(first_name=request.POST.get('first_name'), \
                              last_name=request.POST.get('last_name'), \
                              dob=request.POST.get('dob'), \
                              gender=request.POST.get('gender'), \
                              )
        patient_obj.save()

        return redirect('/dashboard/view/')

def get_details(request,id):
    patient = Patient.objects.get(pk=id)

    patient_dict = {
        'id': patient.id,
        'first_name': patient.first_name,
        'last_name': patient.last_name,
        'dob': patient.dob,
        'gender':patient.gender
    }

    return render(request, 'view_patient.html',patient_dict)

def delete_patient(request):
    pid = request.GET.get('patient_id')
    patient = Patient.objects.get(pk=pid)
    patient.delete()

    return JsonResponse({'success':True})

def edit_info(request,id):
    patient = Patient.objects.get(pk=id)

    patient_dict = {
        'id': patient.id,
        'first_name': patient.first_name,
        'last_name': patient.last_name,
        'dob': patient.dob,
        'gender': patient.gender
    }
    return render(request,'edit_info.html',patient_dict)

def save_changes(request,id):
    Patient.objects.filter(id=id).update(first_name=request.POST.get('first_name'),
                                         last_name=request.POST.get('last_name'),
                                         dob=request.POST.get('dob'),
                                         gender=request.POST.get('gender'),
                                         )

    return redirect('/dashboard/view/')
