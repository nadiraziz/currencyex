from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from .form import ContactForm
from django.core.mail import send_mail

# home
from .models import Services


def home(request):
    news = Services.objects.all()
    services = Services.objects.all()
    form = ContactForm()
    if request.method == "POST":
        message_name = request.POST['name']
        message_email = request.POST['email']
        message_country = request.POST['country']
        message_phone = request.POST['phone_no']
        message = request.POST['message']

        all_message = f'Contact form Exchange Currency \n Name:{message_name} \n Email: ' \
                      f'{message_email}\n Phone Number: {message_phone}\n Country: {message_country}\n Message:' \
                      f' {message}\n'

        send_mail(
            message_name,
            all_message,
            settings.EMAIL_HOST_USER,
            ['nadirkkdeveloper@gmail.com'],
            fail_silently=True

        )
        messages.success(request, 'Success!')
        return redirect('home')
    context = {
        'news': news,
        'services': services,
        'form': form
    }
    return render(request, 'index.html', context=context)


# news
def news(request):
    news = Services.objects.all()
    context = {
        'news': news
    }
    return render(request, 'news.html', context=context)


# exchange
def exchange(request):
    return render(request, 'exchange.html')


# services
def services(request):
    services = Services.objects.all()
    context = {
        'services': services
    }
    return render(request, 'services.html', context=context)


# about
def about(request):
    return render(request, 'about.html')


# contact
def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        message_name = request.POST['name']
        message_email = request.POST['email']
        message_country = request.POST['country']
        message_phone = request.POST['phone_no']
        message = request.POST['message']

        all_message = f'Contact form Exchange Currency \n Name:{message_name} \n Email: ' \
                      f'{message_email}\n Phone Number: {message_phone}\n Country: {message_country}\n Message:' \
                      f' {message}\n'

        send_mail(
            message_name,
            all_message,
            settings.EMAIL_HOST_USER,
            ['nadirkkdeveloper@gmail.com'],
            fail_silently=True

        )

        messages.success(request, 'Success!')
        return render(request, 'contact.html', {'form': form})

    return render(request, 'contact.html', {'form': form})