from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from patient.models import PatientReading  # import from patient app
import requests
from vitals.models import Vitals
from django.http import JsonResponse
from .models import CallRequest

# -------------------- ESP CONFIG --------------------
ESP_IP = "http://192.168.43.125"   # 🔴 CHANGE this to your ESP IP


# -------------------- LOGIN --------------------
def doctor_login(request):
    error = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('doctor_dashboard')
        else:
            error = 'Invalid login credentials'
    return render(request, 'doctor/login.html', {'error': error})


# -------------------- DASHBOARD --------------------
def doctor_dashboard(request):

    try:
        r = requests.get(f"{ESP_IP}/vitals", timeout=3)
        data = r.json()

        pulse = data.get("pulse", "--")
        temperature = data.get("temperature", "--")

    except:
        pulse = "--"
        temperature = "--"

    context = {
        "pulse": pulse,
        "temperature": temperature,
        "time": "Live"
    }

    return render(request, "doctor/doctor_dashboard.html", context)


# -------------------- LIVE VITALS API --------------------
def get_latest_vitals(request):

    try:
        r = requests.get(f"{ESP_IP}/vitals", timeout=3)
        data = r.json()

        return JsonResponse({
            "pulse": data.get("pulse", "--"),
            "temperature": data.get("temperature", "--"),
            "time": "Live"
        })

    except:
        return JsonResponse({
            "pulse": "--",
            "temperature": "--",
            "time": "--"
        })
# -------------------- MEDICINE DISPENSING API --------------------
def dispense_medicine(request):
    motor = request.GET.get("motor")
    qty = request.GET.get("qty")

    try:
        url = f"{ESP_IP}/vend?motor={motor}&qty={qty}"
        response = requests.get(url, timeout=10)

        if response.text.strip() == "DISPENSE_DONE":
            return JsonResponse({
                "status": "success",
                "message": "Medicine dispensed successfully"
            })
        else:
            return JsonResponse({
                "status": "error",
                "message": "Motor error while dispensing"
            })

    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": "ESP not reachable"
        })

def check_call(request):
    call = CallRequest.objects.filter(active=True).first()

    if call:
        return JsonResponse({
            "calling": True,
            "room": call.room_name
        })
    else:
        return JsonResponse({"active": False})   