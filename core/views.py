from django.shortcuts import render
from django.http import HttpResponse
from .models import StolenItem

# Create your views here.

def home(request):
    stolen_item = None
    if request.method == "GET":
        serial_number = request.GET.get('serial_number')
        if serial_number:
            stolen_item = StolenItem.objects.filter(serial_number=serial_number).first()
    return render(request, 'index.html', {'stolen_item': stolen_item})



from django.shortcuts import render, redirect
from django.urls import reverse
from .models import StolenItem

def report(request):
    if request.method == "POST":
        item_name = request.POST.get("item_name")
        serial_number = request.POST.get("serial_number")
        brand = request.POST.get("brand")
        model = request.POST.get("model")
        color = request.POST.get("color")
        description = request.POST.get("description", "")
        contact_phone = request.POST.get("contact_phone")

        # Create and save the stolen item report
        try:
            stolen_item = StolenItem.objects.create(
                item_name=item_name,
                serial_number=serial_number,
                brand=brand,
                model=model,
                color=color,
                description=description,
                contact_phone=contact_phone
            )
            # Redirect to success page
            return redirect(reverse('success'))
        except Exception as e:
            # Redirect to error page
            return redirect(reverse('error'))
    return render(request, "report.html")




def success(request):
    return render(request, 'success.html')

def error(request):
    return render(request, 'error.html')

