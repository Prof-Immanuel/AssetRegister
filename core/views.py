from django.shortcuts import render
from .models import StolenItem
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import StolenItem, Item, CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    stolen_item = None
    if request.method == "GET":
        serial_number = request.GET.get('serial_number')
        if serial_number:
            stolen_item = StolenItem.objects.filter(serial_number=serial_number).first()
    return render(request, 'index.html', {'stolen_item': stolen_item})


def item_register(request):
    if request.method == "POST":
        item_name = request.POST.get("item_name")
        serial_number = request.POST.get("serial_number")
        brand = request.POST.get("brand")
        model = request.POST.get("model", "")
        color = request.POST.get("color", "")
        owner_phone = request.POST.get("owner_phone")

        # Check if item with the same serial number exists
        if Item.objects.filter(serial_number=serial_number).exists():
            messages.error(request, "An item with this serial number is already registered.")
            return redirect("item_register")

        # Save to database
        item = Item(
            item_name=item_name,
            serial_number=serial_number,
            brand=brand,
            model=model,
            color=color,
            owner_phone=owner_phone
        )
        item.save()

        messages.success(request, "Item registered successfully!")
        return redirect("dashboard") 

    return render(request, "item_register.html")


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


# Signup View
def signup_view(request):
    if request.method == 'POST':
        phone = request.POST['phone_number']
        password = request.POST['password']
        if CustomUser.objects.filter(phone=phone).exists():
            messages.error(request, "Phone number already registered")
        else:
            user = CustomUser.objects.create_user(phone=phone, password=password)
            login(request, user)
            messages.success(request, "Signup successful! Please login.")
            return redirect('dashboard')
    return render(request, 'signup.html')

# Login View
def login_view(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        password = request.POST['password']

        user = authenticate(request, username=phone_number, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid phone number or password')

    return render(request, 'login.html')
# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

# Dashboard View
@login_required(login_url='login')
def dashboard(request):
    items = Item.objects.filter(owner_phone=request.user.phone)
    return render(request, 'dashboard.html', {'items': items})



def success(request):
    return render(request, 'success.html')

def error(request):
    return render(request, 'error.html')

