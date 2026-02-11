from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Blog, Category

# Create your views here.
# Same name as the '<int:category_id>/'
def posts_by_category(request,category_id):
    posts_by_category_id = Blog.objects.filter(status="published",category=category_id)
    # categories = Category.objects.all()

    
    # When using the get function in the objects we need to enclose it in a try and except
    # block. We use the try and except to redirect the user.
    # We use the get_objects_or_404 when we want to desplay a 404 page
    category_name  = get_object_or_404(Category, pk=category_id)

    # try:
    #     category_name = Category.objects.get(pk=category_id)
    # except:
    #     return redirect('home')
    
    context = {
        'posts_by_category_id' : posts_by_category_id,
        # 'categories': categories, - sending it individually to each page
        'category_name': category_name
    }
    return render(request, 'category.html',context=context)
