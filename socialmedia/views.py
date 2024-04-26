from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    all_posts = Post.objects.all()
    context = {'posts':all_posts}
    return render(request, 'socialmedia\home.html',context)