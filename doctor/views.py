from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from patient.models import PatientReading  # import from patient app


def doctor_login(request):
    error = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('doctor_dashboard')  # We’ll create this next
        else:
            error = 'Invalid login credentials'
    return render(request, 'doctor/login.html', {'error': error})

def doctor_dashboard(request):
    readings = PatientReading.objects.all().order_by('-id')  # latest first
    return render(request, 'doctor/dashboard.html', {'readings': readings})
    