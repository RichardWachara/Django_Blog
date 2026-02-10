from django.db import models

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