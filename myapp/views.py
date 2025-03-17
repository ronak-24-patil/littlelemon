from django.shortcuts import render
from .forms import CustomerForm

def customer_form(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            # Process the data (e.g., save to the database)
            print("Form data:", form.cleaned_data)
    else:
        form = CustomerForm()
    return render(request, 'customer_form.html', {'form': form})