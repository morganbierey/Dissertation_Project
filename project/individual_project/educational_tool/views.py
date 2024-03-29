from django.shortcuts import render
from django.http import HttpResponse
from educational_tool.models import Category
from educational_tool.models import Page
from educational_tool.models import video
from educational_tool.models import exercise
from educational_tool.models import topic
from educational_tool.models import tutorial
from educational_tool.forms import UserForm, UserProfileForm
import sys
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required






# Create your views here.
def index(request):
  # Query the database for a list of ALL categories currently stored.
    # Order the categories by the number of likes in descending order.
    # Retrieve the top 5 only -- or all if less than 5.
    # Place the list in our context_dict dictionary (with our boldmessage!)
    # that will be passed to the template engine.

    # Render the response and send it back!
    return render(request, 'educational_tool/index.html')

def base(request):
    
    return render(request, 'educational_tool/base.html')

def pycompiler(request):
    # context_dict = {'boldmessage': 'Test your code here using the compiler provided '}
    return render(request, 'educational_tool/pycompiler.html') 

def compilerbase(request,p_id):
    context_dict = {}
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

      context_dict['code'] = codeareadata 
      context_dict['output'] = output

    except Exception as e:
      #else return error
      output = open('file.txt','r').read()
      sys.stdout = original_stdout
      output = e
    # context_dict = {'boldmessage': 'Test your code here using the compiler provided '}
    context_dict = {}
    context_dict['exercises'] = exercise.objects.filter(id=p_id).values().first()
    try:
      context_dict['code'] = codeareadata 
      context_dict['output'] = output
    except Exception as e:
      print(context_dict)


    print(context_dict)


    return render(request, 'educational_tool/compilerbase.html', context=context_dict)  

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
  return render(request,'educational_tool/pycompiler.html',{"code":codeareadata, "output":output})


    
def about(request):
    # return HttpResponse("Educational coding app! THIS IS the abput page")
    context_dict = {'boldmessage': 'This tutorial has been put together by Morgan Bierey'}
    return render(request, 'educational_tool/about.html', context=context_dict)

def show_tutorial(request,tut_id):
    context_dict = {}
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

      context_dict['code'] = codeareadata 
      context_dict['output'] = output

    except Exception as e:
      #else return error
      output = open('file.txt','r').read()
      sys.stdout = original_stdout
      output = e
    # context_dict = {'boldmessage': 'Test your code here using the compiler provided '}
    context_dict = {}
    context_dict['tutorial'] = tutorial.objects.get(id=tut_id)
    try:
      context_dict['code'] = codeareadata 
      context_dict['output'] = output
    except Exception as e:
      print(context_dict)


    print(context_dict)

    
    
    return render(request, 'educational_tool/tutorial.html',context=context_dict)


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

def show_video(request, v_id):
  context_dict = {}
  context_dict['video'] = video.objects.get(url=v_id)
    
  return render(request, 'educational_tool/video.html', context=context_dict)

def show_topic(request, t_id):
    
    context_dict = {}
    context_dict['topic'] = topic.objects.get(id=t_id)
    return render(request, 'educational_tool/topic.html', context=context_dict)


def register(request):
  # A boolean value for telling the template
  # whether the registration was successful.
  # Set to False initially. Code changes value to
  # True when registration succeeds.
  registered = False

  # If it's a HTTP POST, we're interested in processing form data.
  if request.method == 'POST':
    # Attempt to grab information from the raw form information.
    # Note that we make use of both UserForm and UserProfileForm.
    user_form = UserForm(request.POST)
    profile_form = UserProfileForm(request.POST)
  
  # If the two forms are valid...
    if user_form.is_valid() and profile_form.is_valid():
  # Save the user's form data to the database.
      user = user_form.save()

  # Now we hash the password with the set_password method.
  # Once hashed, we can update the user object.
      user.set_password(user.password)
      user.save()

      # Now sort out the UserProfile instance.
      # Since we need to set the user attribute ourselves,
      # we set commit=False. This delays saving the model

      # until we're ready to avoid integrity problems.
      profile = profile_form.save(commit=False)
      profile.user = user

      # Did the user provide a profile picture?
      # If so, we need to get it from the input form and
      #put it in the UserProfile model.
      if 'picture' in request.FILES:
        profile.picture = request.FILES['picture']

      # Now we save the UserProfile model instance.
      profile.save()

      # Update our variable to indicate that the template
      # registration was successful.
      registered = True
    else:
      # Invalid form or forms - mistakes or something else?
      # Print problems to the terminal.
      print(user_form.errors, profile_form.errors)
  else:
    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    user_form = UserForm()
    profile_form = UserProfileForm()

# Render the template depending on the context.
  return render(request,'educational_tool/register.html', context = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})




def user_login(request):
  # If the request is a HTTP POST, pull out the relevant information.
  if request.method == 'POST':
    # collect username & password provided by the user.
    # This information is obtained from the login form.
    # We use request.POST.get('<variable>') as opposed
    # to request.POST['<variable>'], because the
    # request.POST.get('<variable>') returns None if the
    # value does not exist, while request.POST['<variable>']
    # will raise a KeyError exception.
    username = request.POST.get('username')
    password = request.POST.get('password')
    # Use Django's machinery to attempt to see if the username/password
    # combination is valid - a User object is returned if it is.
    user = authenticate(username=username, password=password)
    # If we have a User object, the details are correct.
    # If None (Python's way of representing the absence of a value), no user
    # with matching credentials was found.
    if user:
    # Is the account active? It could have been disabled.
      if user.is_active:
        # If the account is valid and active, we can log the user in.
        # We'll send the user back to the homepage.
        login(request, user)
        return redirect(reverse('educational_tool:login'))
      else:
        # An inactive account was used - no logging in!
        return HttpResponse("Your CodeJutsu account is disabled.")
    else:
      # Bad login details were provided. So we can't log the user in.
      print(f"Invalid login details: {username}, {password}")
      return HttpResponse("Invalid login details supplied.")
    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
  else:
      # No context variables to pass to the template system, hence the
      # blank dictionary object...
    return render(request, 'educational_tool/login.html')
  

# Use the login_required() decorator to ensure only those logged in can
# access the view.
@login_required
def user_logout(request):
  # Since we know the user is logged in, we can now just log them out.
  logout(request)
  # Take the user back to the homepage.
  return redirect(reverse('educational_tool:index'))

@login_required
def view_profile(request):
    user = request.user
    user_profile = user.userprofile

    context = {
        'user_profile': user_profile,
        'user_image': user_profile.picture,
        'user_email': user.email,
        'user_username': user.username,
        'user_profile_picture': user_profile.picture,
    }

    return render(request, 'educational_tool/profile.html', context)
  






