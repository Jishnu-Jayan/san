from django.shortcuts import render
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.template.loader import get_template
from django.views.generic import ListView,DetailView

from sanashapp1.models import contacts


def home(request):


    if request.method == 'POST':
        name = request.POST['cf-name']
        email = request.POST['cf-email']
        number = request.POST['cf-number']
        subject = request.POST['cf-budgets']
        enq_message = request.POST['cf-message']

        html_message = render_to_string('email.html',{'name' : name})
        plane_massage = strip_tags(html_message)
        message = EmailMultiAlternatives(
            subject="Thank you for Subscribing",
            body=plane_massage,
            from_email="noreplay@eail.com",
            to=[email],
        )
        message.attach_alternative(html_message,"text/html")
        message.send()
        obj = contacts(
            enquiry_name = name,
            enquiry_email = email,
            enquiry_subject = subject,
            enquiry_phone = number,
            enquiry_message = enq_message,

            )
        obj.save()


    return render(request,'index.html')

