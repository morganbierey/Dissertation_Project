from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import datetime
from django.conf import settings 
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'


    def __str__(self):
        return self.name
        
class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class exercise(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=128, unique=True)
    problem = models.CharField(max_length=5000, unique=True)

    class Meta:
        verbose_name_plural = 'exercises'

class tutorials(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    paragraph = models.CharField(max_length=1000, unique=True)
    expected_ouput = models.CharField(max_length=128, unique=True)
    question =  models.CharField(max_length=128, unique=True)
    correct_answer = models.CharField(max_length=128, unique=True) #strign based question
    user_answer = models.CharField(max_length=128, unique=True) #string based questions
    coding_answer = models.CharField(max_length=128, unique=True) # the expected output of code 
    user_coding_answer = models.CharField(max_length=128, unique=True) # might not need,, user can compare their own answe to expected answer
    # correct_answer will be compared to the input box - user_answer 

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    picture = models.ImageField(upload_to ='profile_images', blank=True)
    author = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class project(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=128, unique=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE) # userprofile that made the project - author
    published = models.DateField(datetime.date.today())
    upload_file = models.FileField(upload_to= settings.MEDIA_ROOT , max_length=254) # CHECK IF SOMETHING BREAKS I THINK IT UPLOADS TO media directory  FILES
    is_private_project =  models.BooleanField(default=False)
    project_summary = models.CharField(max_length=128, unique=True)

class video(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=128, unique=True)
    url = models.CharField(max_length=5000, unique=True)
    # picture = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # UserProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE) # userprofile that uploaded the video - author

    class Meta:
        verbose_name_plural = 'videos'

    def save(self, *args, **kwargs):
        self.url = self.url
        super(video, self).save(*args, **kwargs)


    def __str__(self):
        return self.title





