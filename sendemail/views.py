from django.http import BadHeaderError, HttpResponse
from django.shortcuts import redirect, render
from MyContact.forms import ContactForm
from django.core.mail import send_mail

import sendemail 

# Create your views here.
def contactView(request):
    if request.method == 'GET':
        formx = ContactForm()
    else:
        formx = ContactForm(request.POST)
        if formx.is_valid():
            email_list = []
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            to_email = form.cleaned_data['to_email']
            email_list.append(to_email)

            try:
                send_mail(subject, message, from_email, email_list)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form1': formx})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')