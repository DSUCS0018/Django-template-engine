from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {'name': 'Ankita'})
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to MyApp!")

def products(request):
    products = [
        {'name': 'Laptop', 'price': 1000},
        {'name': 'Phone', 'price': 500},
        {'name': 'Tablet', 'price': 300}
    ]
    return render(request, 'home.html', {'products': products})
from .forms import ContactForm

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)  # Handle form data
    return render(request, 'form.html', {'form': form})
# myapp/views.py


def contact(request):
    return HttpResponse("This is the contact page.")
# myapp/views.py
from django.http import HttpResponse

def form(request):
    return HttpResponse("This is the form page.")
