from django.shortcuts import render,redirect
from .models import PatientReading
import random
import string


def welcome(request):
    return render(request, 'patient/welcome.html')

def instructions(request):
    return render(request, 'patient/instructions.html')

def simulate_readings(request):
    if request.method == 'POST':
        temperature = float(request.POST.get('temperature'))
        pulse = int(request.POST.get('pulse'))

        request.session['temp'] = temperature
        request.session['pulse'] = pulse

        # Save to database
        PatientReading.objects.create(temperature=temperature, pulse=pulse)

        return redirect('video_call')
    return render(request, 'patient/readings.html')
    

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


