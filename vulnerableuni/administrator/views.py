from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
# Create your views here.

def home(request):
    context = {
        'title':'University Home Page'
    }
    return render(request, 'administrator/home.html', context)

def about(request):
    context = {
        'title': 'Blogging using template'
    }
    return render(request, 'blog/about.html', context)

def xss(request):
    if request.user.is_authenticated:
        q=request.GET.get('q','')
        #f=FAANG.objects.filter(company=q)
        if f:
            args={"company":f[0].company,"ceo":f[0].info_set.all()[0].ceo,"about":f[0].info_set.all()[0].about}
            return render(request,'administrator/xss.html',args)
        else:
            return render(request,'administrator/xss.html', {'query': q})
    else:
        return redirect('login')