from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Vitals
import json

@csrf_exempt
def receive_vitals(request):
    if request.method == "POST":
        data = json.loads(request.body)

        patient_id = data.get("patient_id")
        pulse = data.get("pulse")

        Vitals.objects.create(
            patient_id=patient_id,
            pulse=pulse
        )

        return JsonResponse({"status": "pulse received"})

    # 👇 ADD THIS PART
    return JsonResponse({"message": "Use POST to send vitals"})
