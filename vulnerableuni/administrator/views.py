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
    return render(request, 'administrator/about.html', context)

def search(request):
     q = request.GET.get('search','')
     
     return render(request,'administrator/search.html',{'query':q})

def xss(request):
    '''if request.user.is_authenticated:
        q=request.GET.get('q','')
        #f=FAANG.objects.filter(company=q)
        if f:
            args={"company":f[0].company,"ceo":f[0].info_set.all()[0].ceo,"about":f[0].info_set.all()[0].about}
            return render(request,'administrator/xss.html',args)
        else:
            return render(request,'administrator/xss.html', {'query': q})
    else:
        return redirect('login')'''
    return render(request, 'administrator/xss.html')

def labs(request):
    
    return render(request, 'administrator/labs.html')