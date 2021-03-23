"""hospital_managment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from patient.view import dashboard


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/view/',dashboard.patient_data,name='Patients'),
    path('dashboard/add/',dashboard.add_patient,name='Add New Patient'),
    path('submit/data/',dashboard.submit_data,name='Submit'),
    path('dashboard/detail/?patient_id=<int:id>', dashboard.get_details, name='details'),
    path('delete/patient/', dashboard.delete_patient, name='Delete'),
    path('dashboard/edit/?Patient_id=<int:id>', dashboard.edit_info, name='editinfo'),
    path('save/changes/<int:id>', dashboard.save_changes, name='save_changes'),


]
