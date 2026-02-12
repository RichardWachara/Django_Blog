from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=10,unique=True)
    created_at = models.DateTimeField(auto_now_add=True) # Auto add now is the first time the object is created
    updated_at = models.DateTimeField(auto_now=True) # Auto add is updated every time the models is saved

    class Meta:
        verbose_name_plural = "Categories"

    # self refers to the current instance of the class.
    def __str__(self):
        return self.category_name

# Choices to make a dropdown

STATUS_CHOICES = (
    ("draft", "Draft"),
    ("published","Published")
)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    #URL-safe label used to uniquely identify a blog. Normally a heading separated with hyphens.
    slug = models.SlugField(max_length=150,unique=True,blank=True)
    # Each blog has to be associated with a one category. Once a category is deleted we need to delete all the blogs in that category(CASCADE)
    # This is a one to many relationship.
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to="uploads/%Y/%m/%d")
    short_description = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=10000)
    status = models.TextField(choices=STATUS_CHOICES,default='draft')
    is_featured =  models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) # Auto add now is the first time the object is created
    updated_at = models.DateTimeField(auto_now=True) # Auto add is updated every time the models is saved

    def __str__(self):
        return self.title


class About(models.Model):
    about_heading = models.TextField(max_length=100)
    about_description = models.TextField(max_length=200)

    def __str__(self):
        return self.about_heading
    
class Social_Links(models.Model):
    link_header = models.CharField(max_length=50)
    link_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.link_header