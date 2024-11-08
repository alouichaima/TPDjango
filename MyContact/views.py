from django.http import HttpResponse
from django.shortcuts import render
from MyContact.forms import ContactForm, contactform3
from MyContact.models import Contact

# Create your views here.
def controlform1(request):
    if request.method == 'POST':
        f = request.POST.get('firstname')
        l = request.POST.get('lastname')
        e = request.POST.get('email')
        m = request.POST.get('message')
        
        # Create a new Contact object
        Contact.objects.create(firstname=f, lastname=l, email=e, message=m)
        
        return HttpResponse('<h2>Data has been submitted</h2>')
    
    return render(request, "myform1.html")

def controleform2(request):
    if request.method == 'POST':
        f = request.POST.get('firstname')
        l = request.POST.get('lastname')
        e = request.POST.get('email')
        m = request.POST.get('message')
        
        # Create a new Contact object
        Contact.objects.create(firstname=f, lastname=l, email=e, message=m)
        
        return HttpResponse('<h2>Data has been submitted</h2>')
    else:
        form=ContactForm()
    
    return render(request, "myform2.html",{'form':form})

def controleform3(request):
    if request.method == 'POST':
        form = contactform3(request.POST)
        if form.is_valid():  # Check if the form is valid
            form.save()  # Save the form data to the database
            return HttpResponse('<h2>Data has been submitted</h2>')  # Success message
    else:
        form = contactform3()  # Create an empty form
    return render(request, "myform3.html", {'mycontactform3': form})  # Render the form
        