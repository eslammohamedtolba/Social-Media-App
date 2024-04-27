from django.shortcuts import render, redirect
from .models import Post, UserProfile
# Import authentication libraries
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required



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
    main_profile = UserProfile.objects.get(user = request.user)
    if request.method == 'POST':
        postContent = request.POST.get('content')
        postImage = request.FILES.get('Postimage')
        # Create post for the entered post info
        new_post = Post(user_profile=main_profile,content=postContent,image=postImage)
        new_post.save()
        return redirect('home')
    # Find all posts
    all_posts = Post.objects.filter(user_profile = main_profile) | Post.objects.filter(user_profile__in=main_profile.friends.all())
    all_posts = all_posts.order_by('-created_at')
    # Find all may friends
    if main_profile is not None:
        current_friends = main_profile.friends.all()
        recommended_profiles = UserProfile.objects.exclude(id=main_profile.id)
        for friend in current_friends:
            recommended_profiles = recommended_profiles.exclude(id=friend.id)
    else:
        recommended_profiles = None
    context = {'posts':all_posts, 
                'mayfriends':recommended_profiles, 
                'main_profile':main_profile}
    return render(request, 'socialmedia/home.html',context)

@login_required
def userProfile(request, pk):
    # Find user profile
    userpro = UserProfile.objects.get(id=pk)
    # Find main user profile
    mainuser = request.user
    main_profile = UserProfile.objects.filter(user = mainuser).first()
    is_friend = main_profile.friends.filter(id = userpro.id).exists()
    # Check if the method is post
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'back':
            background_image = request.FILES.get('BackgroundImage')
            if background_image:
                userpro.backgroundImage = background_image
                userpro.save()
        elif form_type == 'front':
            profile_image = request.FILES.get('FrontImage')
            if profile_image:
                userpro.image = profile_image
                userpro.save()
        else:
            # following button clicked then will
            # Check if the user profile is a friend of the main profile
            if not is_friend:
                main_profile.friends.add(userpro)
            else:
                main_profile.friends.remove(userpro)
            main_profile.save()
        return redirect('useraccount', pk = userpro.id)
    # Find posts
    user_posts = Post.objects.filter(user_profile=userpro)
    is_main_profile = (main_profile.id == int(pk))
    context = {'userprofile': userpro, 
                'main_profile':main_profile,
                'posts': user_posts, 
                'is_main_profile': is_main_profile,
                'is_friend':is_friend,
                'num_Friends':len(userpro.friends.all()),
                'friends':userpro.friends.all()}
    return render(request, 'socialmedia\profile.html', context)

@login_required
def setting_privacy(request):
    # Find main user profile
    mainuser = request.user
    main_profile = UserProfile.objects.filter(user = mainuser).first()
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        qoute = request.POST.get('qoute')
        # Check if the username exist or not
        username_exists = False
        for profile in UserProfile.objects.all():
            if profile.user.username == username:
                username_exists = True
                break
        if not username_exists:
            main_profile.user.username = username
        # Verify the password
        if len(password) > 3:
            main_profile.user.password = password
        main_profile.user.email = email
        main_profile.qoute = qoute
        main_profile.user.save()
        main_profile.save()
        return redirect('setting_privacy')
    context = {'main_profile':main_profile}
    print(main_profile.qoute)
    return render(request, 'socialmedia\setting_privacy.html', context)

