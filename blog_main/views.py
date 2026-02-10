# from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category, Blog
# def home(request):
#     return HttpResponse("<h2>Home Page</h2>")

def home(request):
    # Object.all() function fetches all the categories in the database.
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True,status="published")
    posts = Blog.objects.filter(is_featured=False,status="published")
    # print(featured_posts[0].featured_image)
    # The context is a dictionary with key:value pairs the key is what we use to access the data provided in the value.
    
    context = {
        'categories': categories,
        'featured_posts': featured_posts,
        'posts':posts
    }

    # We then provide the context to the page and we can access it on the page when we do this
    return render(request,"index.html",context=context)