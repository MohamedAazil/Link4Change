from django.shortcuts import render, redirect
from .models import Entrepreneur, Investor

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        tags = request.POST['tags']
        entrepreneur = Entrepreneur(title=title, description=description, tags=tags)
        entrepreneur.save()
        return redirect('index')
    return render(request, 'register.html')

def study(request):
    return render(request, 'study.html')

def chatbot(request):
    return render(request, 'chatbot.html')

def mentors(request):
    return render(request, 'mentors.html')

def investors(request):
    if request.method == 'POST':
        name = request.POST['name']
        tags = request.POST['tags']
        investor = Investor(name=name, tags=tags)
        investor.save()
        return redirect('investors')
    
    entrepreneurs = Entrepreneur.objects.all()
    investors = Investor.objects.all()
    matches = []
    for investor in investors:
        investor_tags = set(investor.tags.split(','))
        for entrepreneur in entrepreneurs:
            entrepreneur_tags = set(entrepreneur.tags.split(','))
            if investor_tags & entrepreneur_tags:
                matches.append((investor, entrepreneur))
    
    context = {
        'matches': matches
    }
    return render(request, 'investors.html', context)
