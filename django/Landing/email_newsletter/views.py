from django.shortcuts import render
from django.http import HttpResponse
from .models import PeopleList

# Create your views here.
def home(request):
    name = ''
    city = ''
    phone = ''
    mail = ''

    if request.method == 'POST':
        name = request.POST['name']
        city = request.POST['city']
        phone = request.POST['phone']
        mail = request.POST['mail']
        
    context = {
        'name': name,
        'city': city,
        'phone': phone,
        'mail': mail,
    }
    return render(request, 'email_newsletter/index.html', context)

def test(request):
    return HttpResponse("<h1>I'm a free bitch, baby!</h1>")