from django.shortcuts import render
from contact.contact_form import ContactForm
from django.core.mail import send_mail

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
      name = form.cleaned_data['name'] 
      email = form.cleaned_data['email'] 
      send_mail('Thank you for contacting CodeSmash!', "Hello {0}! Your request has been recieved and we will contact you regarding your inquiry soon! Thanks for everything...".format(name), 'joelbyler@gmail.com', [email])    
    return render(request, 'contact/contactform.html', {
        'form': form
    })

