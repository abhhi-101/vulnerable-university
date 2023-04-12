from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User
import subprocess
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
        #return redirect('login')
        new_username = request.POST.get('new_username')
        return render(request, 'administrator/sxss.html',{"username": new_username} )
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
def clickjacking(request):
    
    return render(request, 'administrator/clickjacking.html')
#====== Exploiting CMD injection
def cmd_lab(request):
    if request.user.is_authenticated:
        if(request.method=="POST"):
            domain=request.POST.get('domain')
            domain=domain.replace("https://www.",'')
            os=request.POST.get('os')
            print(os)
            if(os=='win'):
                command="nslookup {}".format(domain)
            else:
                command = "dig {}".format(domain)
            
            try:
                # output=subprocess.check_output(command,shell=True,encoding="UTF-8")
                process = subprocess.Popen(
                    command,
                    shell=True,
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.PIPE)
                stdout, stderr = process.communicate()
                data = stdout.decode('utf-8')
                stderr = stderr.decode('utf-8')
                # res = json.loads(data)
                # print("Stdout\n" + data)
                output = data + stderr
                print(data + stderr)
            except:
                output = "Something went wrong"
                return render(request,'administrator/cmd_lab.html',{"output":output})
            print(output)
            return render(request,'administrator/cmd_lab.html',{"output":output})
        else:
            return render(request, 'administrator/cmd_lab.html')
    else:
        return redirect('login')
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
def access_control(request):
    return render(request, 'administrator/access_control.html')
#======
def sen_info(request):
    return render(request, 'administrator/info.html')
#======
def cmd(request):
    return render(request, 'administrator/cmd.html')


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