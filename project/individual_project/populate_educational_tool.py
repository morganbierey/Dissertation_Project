import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'individual_project.settings')

import django
django.setup()
from educational_tool.models import Category, Page, video, exercise , topic, tutorial

def populate():
     # First, we will create lists of dictionaries containing the pages
     # # we want to add into each category.
     # # Then we will create a dictionary of dictionaries for our categories.
     # # This might seem a little bit confusing, but it allows us to iterate
     # # through each data structure, and add the data to our models.


        tutorial_pages = [
        {'id':'1','title':'Tutorial1',
        'problem':'Dv7gLpW91DM','answer':'abaa'},
        {'id':'2','title':'Tutorial2',
        'problem':'Y8Tko2YC5hA','answer':'basas'},
        {'id':'3','title':'Tutorial3',
         'problem':'0NO3MJkxm2g','answer':'casas'}]

        topic_pages = [
        {'id':'1','title': ' Loops',
        'content':"""Imagine you have a big box of crayons with 100 different colors, and you want to count how many colors there are. You could start at the first crayon and count  \"1 \", and then move on to the second crayon and count  \"2 \", and so on until you \'ve counted all 100 crayons. This would take a lot of time and effort! 
        Instead, you could use a loop, which is like a special kind of counting machine. You tell the computer to start at the first crayon and count up to 100, and then it does all the counting for you automatically. In the same way, when we \'re writing computer programs, we might have to do something over and over again, like adding up a bunch of numbers or checking a bunch of items in a list.

        Instead of doing the same thing manually each time, we can use loops to make the computer do it for us automatically. Loops help us save time, reduce errors, and make our programs more efficient 
        
        In programming, a loop is a way to repeat a set of instructions multiple times. There are two main types of loops in Python: for loops and while loops.
        
        A "for loop" and a "while loop" are both ways to make the computer do something over and over again, but they work in slightly different ways.

        A "for loop" is like a countdown. Imagine you're counting down from 10 to 1. You start at 10, count down to 9, then 8, then 7, and so on, until you get to 1. In a for loop, we usually know how many times we want to do something, and we count down until we're done.

        A "while loop" is more like a game of tag. Imagine you're playing tag with your friends, and you keep running until someone tags you. You don't know how long you'll be running for, but you keep going until someone tags you. In a while loop, we keep doing something until a certain condition is met.

        So, the main difference is that a "for loop" is used when we know how many times we want to do something, and a "while loop" is used when we don't know how many times we want to do something, but we have a condition that needs to be met before we stop.
        """},
        {'id':'2','title':'Lists ',
        'content':'Y8Tko2YC5hA'},
        {'id':'3','title':'Syntax',
         'content':'0NO3MJkxm2g'}]







        video_pages = [
        {'id':'1','title': 'Intro to why you should code',
        'url':'Dv7gLpW91DM'},
        {'id':'2','title':'What is python ',
        'url':'Y8Tko2YC5hA'},
        {'id':'3','title':'Syntax',
         'url':'0NO3MJkxm2g'}]
        #  {'id':'4','title':'Comments',
        #  'url':''},
        #  {'id':'5','title':'Variables',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'6','title':'Data Types',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'7','title':'Numbers',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'8','title':'Type Casting',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'9','title':'Strings',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'10','title':'Booleans',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'3','title':'Operators',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'3','title':'Lists',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'3','title':'Tuples',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'3','title':'Sets',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'3','title':'Dictionaries',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'3','title':'If/ Else',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'3','title':'While Loops',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'3','title':'For Loops',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'3','title':'Functions',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'3','title':'Arrays',
        #  'url':'0NO3MJkxm2g'},
        #  {'id':'3','title':'Scope',
        #  'url':'0NO3MJkxm2g'}

        excercise_pages = [{'id':'1','title': 'Firstname & lastname',
        'problem': """You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:
            Hello firstname lastname! You just delved into python.

            Function Description:

            Complete the print_full_name function in the editor below.

            print_full_name has the following parameters:

            string first: the first name
            string last: the last name
            Prints

            string: 'Hello  ! You just delved into python' where  and  are replaced with  and .
            Input Format

            The first line contains the first name, and the second line contains the last name.

            Constraints: 

            The length of the first and last names are each ≤ Sample Input 0

            Ross
            Taylor
            Sample Output 0

            Hello Ross Taylor! You just delved into python.
            Explanation 0

            The input read by the program is stored as a string data type. A string is a collection of characters."""},
        {'id':'2','title':'What is python ',
        'problem':'Y8Tko2YC5hA'},
        {'id':'3','title':'Syntax',
         'problem':'0NO3MJkxm2g'} ,]


        python_pages = [
        {'title': 'Official Python Tutorial',
        'url':'http://docs.python.org/3/tutorial/'},
        {'title':'How to Think like a Computer Scientist',
        'url':'http://www.greenteapress.com/thinkpython/'},
        {'title':'Learn Python in 10 Minutes',
         'url':'http://www.korokithakis.net/tutorials/python/'} ]
    
        django_pages = [
            {'title':'Official Django Tutorial',
        'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
        {'title':'Django Rocks',
        'url':'http://www.djangorocks.com/'},
        {'title':'How to Tango with Django',
        'url':'http://www.tangowithdjango.com/'} ]

        other_pages = [
        {'title':'Bottle',
        'url':'http://bottlepy.org/docs/dev/'},
        {'title':'Flask',
        'url':'http://flask.pocoo.org'} ]

        cats = {'Python': {'pages': python_pages,'views':128,'likes':64},
        'Django': {'pages': django_pages,'views':64,'likes':32},
        'Other Frameworks': {'pages': other_pages,'views':32,'likes':16} }

        # If you want to add more categories or pages,
        # add them to the dictionaries above.




        for video_dict in video_pages:
                id = video_dict.get('id')
                title = video_dict.get('title')
                url = video_dict.get('url')
                c = add_vid(id,title,url)
        

        # The code below goes through the cats dictionary, then adds each category,
        # and then adds all the associated pages for that category.
        for cat, cat_data in cats.items():
                c = add_cat(cat,cat_data["views"],cat_data["likes"])
                for p in cat_data['pages']:
                       add_page(c, p['title'], p['url'])

    # Print out the categories we have added.
        for c in Category.objects.all():
                for p in Page.objects.filter(category=c):
                       print(f'- {c}: {p}')
        
        for ex_dict in excercise_pages:
               id = ex_dict.get('id')
               title = ex_dict.get('title')
               problem = ex_dict.get('problem')
               p = add_excercise(id,title,problem)
        
        for topic in topic_pages:
               id = topic.get('id')
               title = topic.get('title')
               content = topic.get('content')
               p = add_top(id,title,content)
        
        for tut in tutorial_pages:
               id = tut.get('id')
               title = tut.get('title')
               problem = tut.get('problem')
               answer = tut.get('answer')
               p = add_tut(id,title,problem,answer)
               


def add_page(cat, title, url, views=0):
        p = Page.objects.get_or_create(category=cat, title=title)[0]
        p.url=url
        p.views=views
        p.save()
        return p

def add_vid(id,title, url):
     v = video.objects.get_or_create(id=id,title=title,url=url)[0]
     v.save()
     return v

def add_cat(name, views=0,likes=0):
        c = Category.objects.get_or_create(name=name,views =views, likes=likes)[0]
        c.save()
        return c



def add_excercise(id,title, problem):
     p = exercise.objects.get_or_create(id=id,title=title,problem=problem)[0]
     p.save()
     return p

def add_top(id,title, content):
       t  = topic.objects.get_or_create(id=id,title=title,content=content)[0]
       print(t)
       t.save()
       return t

def add_tut(id,title,problem,answer):
        tu= tutorial.objects.get_or_create(id=id, title=title, problem=problem, answer=answer)[0]
        print(tu)
        tu.save()
        return tu
       
       




# Start execution here!
if __name__ == '__main__':
    print('Starting educational_tool population script...')
    populate()



