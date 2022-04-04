from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead
from .forms import LeadForm, LeadModelForm
# Create your views here.
def lead_list(request):
    leads = Lead.objects.all()
    context = {
        'leads': leads
    }
    return render(request, 'leads/lead_list.html', context)


def lead_detail(request, pk):
    print(pk)
    lead = Lead.objects.get(id=pk)
    return render(request, 'leads/lead_detail.html', {'lead':lead})


def lead_create(request):
    form = LeadModelForm()
    if request.method == 'POST':
        print('receiving post request')
        form = LeadModelForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            print(first_name)
            form.save()
    return render(request, 'leads/lead_create.html', {'form':form})