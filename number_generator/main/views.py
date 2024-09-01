from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index(request):
    if request.user.is_authenticated:
        return render(request, 'main/dashboard.html')
    else:
        return render(request, 'main/index.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')
