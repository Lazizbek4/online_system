from django.shortcuts import render
from .forms import ContactForm


def index(request):
    return render(request, 'main/index.html')


def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            post = contact_form.save(commit=False)
            post.save()
            print("Success!")
            return render(request, 'main/index.html')
        else:
            return render(request, "main/contact.html", {'form': contact_form})
    else:
        form = ContactForm(None)
    return render(request, 'main/contact.html', {'form': form})


def login(request):
    return render(request, 'account/login.html', context={})


def signup(request):
    return render(request, 'account/signup.html', context={})
