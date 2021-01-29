from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

# Class inherits from base class django.db.models.Model
class Category(models.Model):
    # since unique=True, every category name must be unique
    # we can use default='value' so that field has a default value
    # or whether a value for a field is allowed to be NULL (null=True)
    # We also want to create a max_length constant variable
    MAX_LENGTH = 128 # All uppercase since constant (style)
    name = models.CharField(max_length=MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name) #hi there friend becomes hi-there-friend
        super(Category, self).save(*args, **kwargs)
        
    # changes the category name from 'Categorys' to 'Categories'
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    # the foreign key allows a one-to-many relation with Category class
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=Category.MAX_LENGTH) # stores character data (string)
    url = models.URLField() # stores resource URLs
    views = models.IntegerField(default=0) # stores integers

    def __str__(self):
        return self.title
