from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib import messages

User = get_user_model()


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone = request.POST.get('phone')
        office_name = request.POST.get('office_name')
        issue_category = request.POST.get('issue_category').lower().strip()
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken! try another one')
            return render(request, 'create_user.html')
            
        if password != confirm_password:
            messages.error(request, "Password missmatch!")
            return render(request, 'create_user.html')
            
        user = User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email,
            password = password,
            phone = phone,
            office_name = office_name,
            issue_category = issue_category,
        )
        
        login(request, user)
        if issue_category == 'general':
            return redirect('all_issues')
        return redirect('dashboard')
    return render(request, 'create_user.html')


def office_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "login.html")