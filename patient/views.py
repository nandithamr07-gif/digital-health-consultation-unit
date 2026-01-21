from django.shortcuts import render,redirect
from .models import PatientReading
import random
import string
import requests
from django.http import JsonResponse
from doctor.models import CallRequest


def welcome(request):
    return render(request, 'patient/welcome.html')

def instructions(request):
    return render(request, 'patient/instructions.html')

#def simulate_readings(request):
   # if request.method == 'POST':
     #   temperature = float(request.POST.get('temperature'))
      #  pulse = int(request.POST.get('pulse'))

      #  request.session['temp'] = temperature
       ## request.session['pulse'] = pulse

        # Save to database
       # PatientReading.objects.create(temperature=temperature, pulse=pulse)

       # return redirect('video_call')
    #return render(request, 'patient/readings.html')
    

def video_call(request):
    temp = request.session.get('temp')
    pulse = request.session.get('pulse')

    # 🔹 Generate a unique room name if not already present
    if 'jitsi_room' not in request.session:
        room_name = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        request.session['jitsi_room'] = room_name
    else:
        room_name = request.session['jitsi_room']

    return render(request, 'patient/video_call.html', {
        'temp': temp,
        'pulse': pulse,
        'room_name': room_name
    })


ESP_IP = "http://192.168.43.125"

def patient_dashboard(request):
    try:
        r = requests.get(f"{ESP_IP}/vitals", timeout=3)
        data = r.json()

        pulse = data.get("pulse", "--")
        temperature = data.get("temperature", "--")

    except:
        pulse = "--"
        temperature = "--"

    return render(request, "patient/readings.html", {
        "pulse": pulse,
        "temperature": temperature
    })


def patient_live_vitals(request):
    try:
        r = requests.get(f"{ESP_IP}/vitals", timeout=3)
        data = r.json()

        return JsonResponse({
            "pulse": data.get("pulse", "--"),
            "temperature": data.get("temperature", "--")
        })

    except:
        return JsonResponse({
            "pulse": "--",
            "temperature": "--"
        })
JITSI_ROOM="DHCU-Test-Room"    
def start_call(request):
    patient_id = "P001"

    call, _ = CallRequest.objects.get_or_create(patient_id=patient_id)
    call.room_name = JITSI_ROOM
    call.active = True
    call.save()

    return JsonResponse({"status": "calling"})
