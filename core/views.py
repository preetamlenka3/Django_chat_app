from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SignUpForm

# Create your views here.
def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            # Print for debugging
            print("User created and logged in successfully.")

            return redirect('frontpage')
        else:
            # Print form errors for debugging
            print(form.errors)
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})