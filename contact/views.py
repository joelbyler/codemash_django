from django.shortcuts import render
from contact.contact_form import ContactForm
from django.core.mail import send_mail
from django.shortcuts import redirect

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
      name = form.cleaned_data['name'] 
      email = form.cleaned_data['email'] 
      message = form.cleaned_data['message']
      send_mail('Thank you for contacting CodeSmash!', "Hello {0}! Your request has been recieved and we will contact you regarding your inquiry soon! Thanks for everything... Your Message: {1}".format(name, message), 'joelbyler@gmail.com', [email])    

      return redirect('contact:success')

    return render(request, 'contact/contactform.html', {
        'form': form
    })

def contact_success(request):
    return render(request, 'contact/contactsuccess.html')
