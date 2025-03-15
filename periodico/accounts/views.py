from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("list_news")
        else:
            return render(request, "accounts/login.html", {"error": "Credenciales incorrectas"})
    
    return render(request, "accounts/login.html")

def list_news(request):
    return render(request, "accounts/list.html")

def create_news(request):
    return render(request, "accounts/form.html")