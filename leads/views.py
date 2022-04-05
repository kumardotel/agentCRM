from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.core.mail import send_mail
from django.views.generic import TemplateView, ListView, DetailView,  CreateView, UpdateView, DeleteView
from .models import Lead
from .forms import LeadForm, LeadModelForm
# Create your views here.

class LandingPageView(TemplateView):
    template_name = "landing.html"


class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = leads = Lead.objects.all()



class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = leads = Lead.objects.all()



class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        send_mail(
            subject="A new lead has been created",
            message="You can follow up for further details"
        )
        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(UpdateView):
    queryset = leads = Lead.objects.all()
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

   


# class LeadDeleteView(DeleteView):
#     queryset = leads = Lead.objects.all()
#     template_name = "leads/lead_delete.html"
#     form_class = LeadModelForm

#     def get_success_url(self):
#         return reverse("leads:lead-list")

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/leads/')