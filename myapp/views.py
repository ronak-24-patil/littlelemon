from django.shortcuts import render
from .forms import CustomerForm
from .forms import InputForm
from django.shortcuts import render, redirect
from .forms import LogForm
from .models import Menu

def customer_form(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            # Process the data (e.g., save to the database)
            print("Form data:", form.cleaned_data)
    else:
        form = CustomerForm()
    return render(request, 'customer_form.html', {'form': form})

def form_view(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            # Process the data (e.g., save to the database)
            print("Form data:", form.cleaned_data)
    else:
        form = InputForm()
    return render(request, 'home.html', {'form': form})



def log_view(request):
    if request.method == "POST":
        form = LogForm(request.POST)  # Bind form data
        if form.is_valid():
            form.save()  # Save data to database
            return redirect('success')  # Redirect to a success page
    else:
        form = LogForm()

    return render(request, 'log_form.html', {'form': form})

def about(request):
    about_content = {"about": "Welcome to Little Lemon! We serve fresh and delicious food every day."}
    return render(request, 'about.html', about_content)


def menu(request):
    new_menu = {
        "mains": [
            {"name": "Greek Salad", "price": "$10"},
            {"name": "Pasta Primavera", "price": "$12"},
            {"name": "Margherita Pizza", "price": "$15"},
            {"name": "Grilled Salmon", "price": "$18"},
        ]
    }
    return render(request, 'menu.html', new_menu)

def menu_card(request):
    new_menu = Menu.objects.all()  # Fetch all menu items from the database
    return render(request, 'menu_card.html', {'menu': new_menu})
