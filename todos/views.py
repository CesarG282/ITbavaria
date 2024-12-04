from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def helloworld(request):
    return render(request, 'signup.html', {
        'form': UserCreationForm
    })