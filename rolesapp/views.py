from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import login
from .forms import userRegistrationForm, dealerRegistrationForm

def customer_registration(request):
    if request.method == 'POST':
        form = userRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_user = True
            user.save()
            login(request, user)
            return redirect('customer_dashboard')  # Redirect to customer dashboard
    else:
        form = userRegistrationForm()
    return render(request, 'customer_registration.html', {'form': form})

def dealer_registration(request):
    if request.method == 'POST':
        form = dealerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_dealer = True
            user.save()
            login(request, user)
            return redirect('seller_dashboard')  # Redirect to seller dashboard
    else:
        form = dealerRegistrationForm()
    return render(request, 'seller_registration.html', {'form': form})