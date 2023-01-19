from django.shortcuts import render
from django.http import HttpResponse
from educational_tool.models import Category
from educational_tool.models import Page
import sys

# Create your views here.
def index(request):
  # Query the database for a list of ALL categories currently stored.
    # Order the categories by the number of likes in descending order.
    # Retrieve the top 5 only -- or all if less than 5.
    # Place the list in our context_dict dictionary (with our boldmessage!)
    # that will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Why Learn Code?'
    context_dict['categories'] = category_list
    # Render the response and send it back!
    return render(request, 'educational_tool/index.html', context=context_dict)

def pycompiler(request):
    # context_dict = {'boldmessage': 'Test your code here using the compiler provided '}
    return render(request, 'educational_tool/pycompiler.html')  

def runcode(request):
  if request.method == "POST":
    codeareadata = request.POST['codearea']
    try:
      #save original standard output reference

      original_stdout = sys.stdout
      sys.stdout = open('file.txt','w') # change standard ouput to the file we created

      #execute code
      exec(codeareadata) #example print("hello")

      sys.stdout = original_stdout # reset original standard output to its orignial value 

      # reads output from file and save in outut variable
      output = open('file.txt','r').read()

    except Exception as e:
      #else return error
      sys.stdout = original_stdout
      output = e

  #return rendered page and send output and codearea data to show on page
  return render(request,'pycompiler.html',{"code":codeareadata, "output":output})


    
def about(request):
    # return HttpResponse("Educational coding app! THIS IS the abput page")
    context_dict = {'boldmessage': 'This tutorial has been put together by Morgan Bierey'}
    return render(request, 'educational_tool/about.html', context=context_dict)

def show_category(request, category_name_slug):
  # Create a context dictionary which we can pass
  # to the template rendering engine.
  context_dict = {}
  try:
    # Can we find a category name slug with the given name?
    # If we can't, the .get() method raises a DoesNotExist exception.
    # The .get() method returns one model instance or raises an exception.
    category = Category.objects.get(slug=category_name_slug)
    # Retrieve all of the associated pages.
    # The filter() will return a list of page objects or an empty list.
    pages = Page.objects.filter(category=category)
    # Adds our results list to the template context under name pages.
    context_dict['pages'] = pages
    # We also add the category object from
    # the database to the context dictionary.
    # We'll use this in the template to verify that the category exists.
    context_dict['category'] = category
  except Category.DoesNotExist:
    # We get here if we didn't find the specified category.
    # Don't do anything -
    # the template will display the "no category" message for us.
    context_dict['category'] = None
    context_dict['pages'] = None
    # Go render the response and return it to the client.
  return render(request, 'educational_tool/category.html', context=context_dict)


