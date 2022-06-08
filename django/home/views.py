from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import reverse

# Create your views here.
# Request -> Response
# Request Handler
# called an Action in other frameworks

def home(request):
    if 'logged_in' in request.COOKIES and 'username' in request.COOKIES:
            context = {
                'username':request.COOKIES['username'],
                'login_status':request.COOKIES.get('logged_in'),
            }
            return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')

def login(request):
    # Return home page if cookie exists, otherwise retrun login page
    if request.method == "GET":
        # getting cookies
        if 'logged_in' in request.COOKIES and 'username' in request.COOKIES:
            context = {
                'username':request.COOKIES['username'],
                'login_status':request.COOKIES.get('logged_in'),
            }
            return render(request, 'home.html', context)
        else:
            return render(request, 'login.html')

    # Submit username and password, respond with home page and pass parameters 
    if request.method == "POST":
        username=request.POST.get('email')
        context = {
                'username':username,
                'login_status':'TRUE',
            }
        response = render(request, 'home.html', context)

        # setting cookies
        response.set_cookie('username', username)
        response.set_cookie('logged_in', True)
        return response


def logout(request):
    # When user signs out redirect them to the home page and delete cookies
    response = HttpResponseRedirect(reverse('home'))
    response.delete_cookie('username')
    response.delete_cookie('logged_in')
    return response