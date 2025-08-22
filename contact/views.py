from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactManualForm, ContactModelForm

def home(request):
    return render(request, 'contact/home.html')

def contact_manual(request):
    if request.method == 'POST':
        form = ContactManualForm(request.POST)
        if form.is_valid():
            from .models import Contact
            Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact_manual')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactManualForm()
    return render(request, 'contact/contact_manual.html', {'form': form})


def contact_modelform(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact_modelform')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactModelForm()
    return render(request, 'contact/contact_modelform.html', {'form': form})
