from django.db import models

# Create your models here.

# Class inherits from base class django.db.models.Model
class Category(models.Model):
    # since unique=True, every category name must be unique
    # we can use default='value' so that field has a default value
    # or whether a value for a field is allowed to be NULL (null=True)
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    # changes the category name from 'Categorys' to 'Categories'
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    # the foreign key allows a one-to-many relation with Category class
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128) # stores character data (string)
    url = models.URLField() # stores resource URLs
    views = models.IntegerField(default=0) # stores integers

    def __str__(self):
        return self.title
