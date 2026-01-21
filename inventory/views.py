from django.shortcuts import render
from .models import Medicine
from django.db import models
from django.shortcuts import get_object_or_404, redirect
def operator_dashboard(request):
    medicines = Medicine.objects.all()
    low_stock_medicines = Medicine.objects.filter(
        quantity__lte=models.F('low_stock_threshold')
    )

    context = {
        'medicines': medicines,
        'low_stock_medicines': low_stock_medicines,
    }
    return render(request, 'inventory/operator_dashboard.html', context)

def refill_medicine(request, med_id):
    medicine = get_object_or_404(Medicine, id=med_id)

    if request.method == 'POST':
        refill_qty = int(request.POST.get('refill_quantity'))
        medicine.quantity += refill_qty
        medicine.save()
        return redirect('operator_dashboard')

    return render(request, 'inventory/refill_medicine.html', {'medicine': medicine})