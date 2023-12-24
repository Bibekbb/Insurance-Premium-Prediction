from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import joblib
from .forms import CustomerForm, CustomerLoginForm
from .models import UserCreateForm
from django.contrib.auth.models import User

model = joblib.load('static/random_forest')


# Create your views here.
def home(request):
    return render(request, 'base.html')


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def prediction(request):
    if request.method == 'POST':
        try:
            age = int(request.POST.get('age'))
            sex = int(request.POST.get('sex'))
            bmi = float(request.POST.get('bmi'))  
            children = int(request.POST.get('children'))
            smoker = int(request.POST.get('smoker'))
            region = int(request.POST.get('region'))

            print(age, sex, bmi, children, smoker, region)

            pred = model.predict([[age, sex, bmi, children, smoker, region]])

            print(pred)
            output = {
                'output': pred,
            }

            return render(request, 'prediction.html', output)
        except ValueError as e:
            # Handle the conversion error, e.g., by displaying an error message to the user
            print(f"Error: {e}")
            return render(request, 'prediction.html', {'error': 'Invalid input. Please enter numeric values.'})
    else:
        return render(request, 'prediction.html')




def register(request):
    if request.method == "POST":
        fm = CustomerForm(request.POST)
        if fm.is_valid():
            
            new_user = fm.save()
            
            # Corrected authenticate() call with only 'username' and 'password'
            
            new_user = authenticate(
                username=fm.cleaned_data['name'],
                password=fm.cleaned_data['password']
            )
            
            if new_user is not None:
                login(request, new_user)
                return redirect('/')
            else:
                return render(request, 'user/login.html',{'form':fm})
    else:
        fm = CustomerForm()
    return render(request, 'user/register.html', {'form': fm})



def login(request):
    if request.method == "POST":
        form = CustomerLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Authenticate user without passing 'request' explicitly
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = CustomerLoginForm()

    return render(request, 'user/login.html', {'form': form})