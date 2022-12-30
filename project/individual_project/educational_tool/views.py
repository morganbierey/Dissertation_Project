from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'educational_tool/index.html', context=context_dict)
    
def about(request):
    # return HttpResponse("Educational coding app! THIS IS the abput page")
    context_dict = {'boldmessage': 'This tutorial has been put together by Morgan Bierey'}
    return render(request, 'educational_tool/about.html', context=context_dict)