from django.contrib.auth import authenticate, login as auth_login , logout
from django.shortcuts import render, redirect
from .models import Data
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        username = request.POST.get('userid')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # Set session data
            request.session['username'] = username
            return redirect('show')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def user_logout(request):
    logout(request)
    # Clear session data
    request.session.clear()
    return redirect('login')  

@login_required
def create(request):
    if request.POST:
        img=request.FILES.get('photo')
        name = request.POST.get('name')
        age = request.POST.get('age')
        dob=request.POST.get('dob')
        email = request.POST.get('email')
        place = request.POST.get('place')
        job = request.POST.get('job')
        education = request.POST.get('education')
        number = request.POST.get('number')
        instagram =request.POST.get('instagram')
        facebook =request.POST.get('facebook')
        car_or_two_wheel_number=request.POST.get('car_or_two_wheel_number')
       
        new_data = Data(name=name, age=age, email=email, place=place, job=job, education=education, number=number,car_or_two_wheel_number=car_or_two_wheel_number,dob=dob,facebook=facebook,instagram=instagram,img=img)
        new_data.save()

    return render(request, 'create.html')

@login_required
def show(request):
    data = Data.objects.all()
    return render(request, 'show.html', {'data': data})

@login_required
def modify(request):
    return render(request, 'modify.html')


def handler404(request, exception):
    return render(request, '404.html', status=404)

@login_required
def modify(request):
    data=Data.objects.all()
    return render(request, 'modify.html',{'data': data})

@login_required
def dele(request,pk):
    data=Data.objects.get(pk=pk)
    data.delete()
    data=Data.objects.all()
    return render(request, 'modify.html',{'data': data})