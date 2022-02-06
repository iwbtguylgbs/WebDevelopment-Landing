from django.shortcuts import render
from django.http import HttpResponse
from .models import PeopleList, welcome_mail
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create your views here.
def home(request):
    name = ''
    city = ''
    age = ''
    phone = ''
    mail = ''

    context = {
        'name': '',
        'city': '',
        'age': '',
        'phone': '',
        'mail': '',
    }

    if request.method == 'POST':
        print(context)
        name = request.POST['name']
        city = request.POST['city']
        phone = request.POST['phone']
        mail = request.POST['mail']
        age = request.POST['age']
        
        context = {
            'name': name,
            'city': city,
            'age': age,
            'phone': phone,
            'mail': mail,
        }
        print(context)

    if context['mail'] != '':
        #savedata(context)
        #sendmail(context['mail'])
        pass

    return render(request, 'email_newsletter/index.html')

def test(request):
    return HttpResponse("<h1>I'm a free bitch, baby!</h1>")

def savedata(context):
    blank = PeopleList.objects.create(
        name=context["name"],
        city=context["city"],
        number=context["phone"],
        mail=context["mail"]
    )

def sendmail(mail):
    msg = MIMEMultipart()

    from_email = 'lambda.tutoring.ru@gmail.com'
    password = 'lambda_tutoring_ru_QuTyh230_9'
    to_email = mail
    message = welcome_mail

    msg.attach(MIMEText(message, 'html'))
    msg['Subject'] = "Обучение на курсах LambdaLanding!"
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

    print('ПИСЬМО ОТПРАВЛЕНО ##')

def construct_mail():
    pass