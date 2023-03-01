import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'individual_project.settings')

import django
django.setup()
from educational_tool.models import Category, Page, video

def populate():
     # First, we will create lists of dictionaries containing the pages
     # # we want to add into each category.
     # # Then we will create a dictionary of dictionaries for our categories.
     # # This might seem a little bit confusing, but it allows us to iterate
     # # through each data structure, and add the data to our models.


 video_pages = [
        {'id':'1','title': 'Intro to why you should code',
        'url':'Dv7gLpW91DM&list=PLcfakU00Qwfoso7mzGxuSLwVzrQCP6juI&index=3'},
        {'id':'2','title':'what is python ',
        'url':'Y8Tko2YC5hA'},
        {'id':'3','title':'Syntax',
         'url':'0NO3MJkxm2g'} ]



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

def add_page(cat, title, url, views=0):
        p = Page.objects.get_or_create(category=cat, title=title)[0]
        p.url=url
        p.views=views
        p.save()
        return p

def add_cat(name, views=0,likes=0):
        c = Category.objects.get_or_create(name=name,views =views, likes=likes)[0]
        c.save()
        return c


def add_vid(id,title, url):
     v = video.objects.get_or_create(id=id,title=title,url=url)[0]
     v.save()
     return v


# Start execution here!
if __name__ == '__main__':
    print('Starting educational_tool population script...')
    populate()



