from django.shortcuts import render, redirect
from .models import Post, UserProfile
# Import authentication libraries
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
# Create your views here.
def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Create flash messages about username
        checkuser = authenticate(username = username, password = password)
        if checkuser is not None:
            login(request, checkuser)
            return redirect('home')
        else:
            messages.error(request,"the user doesn't exist")
            return redirect('/login')        
    return render(request, 'socialmedia\login.html')
def userlogout(request):
    logout(request)
    return redirect('/login')
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'The username already exists')
            return redirect('/register')
        # Check password length
        if len(password) < 4:
            messages.error(request, 'The password must be at least four characters')
            return redirect('/register')
        # Create the user account
        user = User.objects.create_user(username=username, email=email, password=password)
        # Create UserProfile instance
        user_profile = UserProfile.objects.create(user=user)
        # Save the UserProfile instance
        user_profile.save()
        messages.success(request, 'Account created successfully. Please log in.')
        return redirect('/login')
    else:
        return render(request, 'socialmedia/register.html')
    
@login_required
def home(request):
    # Find all posts
    all_posts = Post.objects.all()

    # Find all may friends
    UsEr = request.user
    user_profile = UserProfile.objects.filter(user=UsEr).first()
    user_friends = user_profile.friends.all()
    all_mayusers = UserProfile.objects.exclude(user=user_profile.user).exclude(friends__in=user_friends)

    context = {'posts':all_posts, 'mayfriends':all_mayusers, 'userprofile':user_profile}
    return render(request, 'socialmedia/home.html',context)