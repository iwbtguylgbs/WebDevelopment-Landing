from django.shortcuts import render
from django.http import HttpResponse
from .models import *
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
    if context["mail"] != '':
        #savedata(context)
        sendmail(context, construct_mail(context))

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

def sendmail(context, page):
    msg = MIMEMultipart()

    from_email = 'lambda.tutoring.ru@gmail.com'
    password = 'lambda_tutoring_ru_QuTyh230_9'
    to_email = context["mail"]
    message = page

    msg.attach(MIMEText(message, 'html'))
    msg['Subject'] = "Обучение на курсах LambdaTutoring!"
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

def construct_mail(context):
    page = welcome_mail_before_name

    NAME = context['name']
    page += NAME
    page += welcome_mail_after_name_before_city

    CITY = context['city']
    page += CITY
    page += welcome_mail_after_city_before_platform

    PLATFORM_COUNT = construct_platforms(CITY)
    page += PLATFORM_COUNT
    page += welcome_mail_after_platform

    images = ''

    for i in range(len(courses_src[context['age']])):
        blank = ''

        blank += blank_course_before
        link = courses_src[context['age']][i]
        blank += link
        blank += blank_course_after
        
        images += blank

    page += images
    page += welcome_mail_after_course_img
    return page

def construct_platforms(city_name):
    try:
        platform_info = PlatformsList.objects.get(city = city_name)
        number = platform_info.number
        adresses = platform_info.adresses
        adresses_array = adresses.split(';')
        adresses = ''
        for i in adresses_array:
            adresses += i
            adresses += '<br>'

        return f'есть {number} площадок по следующим адресам: <br><br>{adresses}'

    except Exception:
        return 'нет площадок в этом городе. '