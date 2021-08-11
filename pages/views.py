from django.shortcuts import render
from django.views.generic import TemplateView
from .models import GetInTouch
# Create your views here.

def HomePageView(request):
        if request.POST:
            model = GetInTouch()
            model.name = request.POST.get('name', '')
            model.email = request.POST.get('email', '')
            model.subject = request.POST.get('subject', '')
            model.message = request.POST.get('message', '')
            model.save()

        return render(request, 'home.html')

def ListView(request):
    return render(request, 'telegram_bot.html')