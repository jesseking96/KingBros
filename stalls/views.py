from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import DetailView,TemplateView
from django.views.generic.edit import FormView
from .models import Stall
from .forms import ContactForm
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
# Create your views here.
class StallListView(ListView):
    model = Stall
    template_name = "stalls/stalls_list.html"

class StallDetailView(DetailView):
    model = Stall
    template_name='stalls/stall_detail.html'

class StallInfoRequest(FormView):
    form_class = ContactForm
    template_name='stalls/get_more_info.html'
    success_url = reverse_lazy('thanks')
    def form_valid(self,form):
        clean_form = form.cleaned_data
        name = clean_form["name"]
        email = clean_form['email']
        phone = clean_form['phone']
        comment = clean_form['comments']
        message_body = render_to_string('pages/email.html',clean_form)
        send_mail(subject="Customer Inquiry",message=message_body,
                    from_email="jesseking96@yahoo.com",
                    recipient_list=["metalandhotdogs@yahoo.com",],
                    fail_silently=False)
        return super().form_valid(form)
