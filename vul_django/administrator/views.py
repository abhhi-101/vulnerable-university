from django.shortcuts import render, redirect
#from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User
import subprocess
from students.models import Company

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
#====== SQL lab
def db(request):
    username = request.GET.get('user','')
    password = request.GET.get('passwd','')
    result = Company.objects.raw("SELECT id, user FROM students_testauth WHERE user='" + username +"' AND passwd='"+ password+"'")
    if result:
        return render(request, 'administrator/db.html', {'res': "Login successfull", 'query': result})
    else:
        return render(request, 'administrator/db.html', {'res': "Wrong Creds",'query':result})


# Learning Labs - content
def labs(request):
    return render(request, 'administrator/labs.html')
#====== XSS
def xss_lab(request):
    if request.user.is_authenticated:
        return render(request, 'administrator/xss.html')
    else:
        return redirect('login')
#====== CSRF 
def csrf_lab(request):
    return render(request, 'administrator/csrf.html')
#====== Access control
def access_control(request):
    return render(request, 'administrator/access_control.html')
#====== Sensitive info
def sen_info(request):
    return render(request, 'administrator/info.html')
#====== Command
def cmd(request):
    return render(request, 'administrator/cmd.html')
#====== SQL 
def db_info(request):
    return render(request, 'administrator/db_info.html')
#====== Debug
def debug_lab(request):
    return render(request, 'administrator/debug.html')
#====== HTTP
def http(request):
    return render(request, 'administrator/http.html')



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