from django.shortcuts import render
from django.http import HttpResponse
# Import the Category model
from rango.models import Category
from rango.models import Page
'''
Each view exists withing views.py as a series of individual functions
We have now created one view called index.
Each view takes at least one argument (an HttpRequest - convention to call
it request) and return one HttpResponse (what we want to send to the client
requesting the view.
'''
def index(request):
    # Query the database for a list of ALL categories currently stored
    # Order the categories by the number of likes in descending order
    # Retrieve the top 5 only -- or all if less than 5
    # Place the list in our context_dict dictionary (with out boldmessage!)
    # that will be passed to the template engine
    category_list = Category.objects.order_by('-likes')[:5] # - denotes that we want the likes in descending order
    page_list = Page.objects.order_by('-views')[:5]
    
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list

    # Note that the first parameter is the template we wish to use
    # Render the response and send it back!
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')

def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception
        # The .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)

        # Retrieve all of the associated pages.
        # The filter() will return a list of page objects or an empty list.
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from
        # the database to the context dictionary
        # We'll use this in the template to verifu that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us.
        context_dict['category'] = None
        context_dict['pages'] = None

    # Go render the response and return it to the client
    return render(request, 'rango/category.html', context=context_dict)
