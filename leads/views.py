from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm

def leadList(request):
    leads = Lead.objects.all()

    context = {
        "leads": leads
    }
    return render(request, "leads/leadList.html", context)

def leadDetail(request, pk):
    print(pk)
    lead = Lead.objects.get(id=pk)
    context = {'lead': lead}
    return render(request, "leads/leadDetail.html", context)

def leadCreate(request):
    form = LeadForm()
    if request.method == 'POST':
        print('receving')
        form = LeadForm(request.POST)
        if form.is_valid():
            print('form valid')
            print(form.cleaned_data)
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            age = form.cleaned_data['age']
    context = {
        "form": LeadForm()
    }
    return render(request, "leads/leadCreate.html", context)