from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User

# To exploit - sXSS and CSRF
def change_username(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = User.objects.get(username=request.user.username)
            new_username = request.POST.get('new_username')
            user.username = new_username
            user.save()
            request.session['username'] = new_username
            return render(request, 'administrator/sxss.html', {"username": new_username})
        else: 
            return render(request, 'administrator/sxss.html',{"old_username":User.objects.get(username=request.user.username)})
    else:
        return redirect('login')
# To exploit - rXSS
def search(request):
    if (request.GET.get('search','')==''):
        return render(request,'administrator/search.html')
    else: 
        q = request.GET.get('search','')
        return render(request,'administrator/search.html',{'query':q})
# To exploit bruteforce attack
def bruteforce(request):
    return render(request, 'administrator/bruteforce.html')
#======




# Learning Labs - content
def labs(request):
    return render(request, 'administrator/labs.html')
#======
def xss_lab(request):
    if request.user.is_authenticated:
        return render(request, 'administrator/xss.html')
    else:
        return redirect('login')
#======
def csrf_lab(request):
    return render(request, 'administrator/csrf.html')
#======



# System Pages
def home(request):
    context = {
        'title':'Vuln University'
    }
    return render(request, 'administrator/home.html', context)
#======
def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'administrator/about.html', context)
#======