from django.contrib import admin
from educational_tool.models import Category, Page, project, video, UserProfile, exercises, tutorials

#second from.. added in ex5.6
# Register your models here.

# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


#class below created chapter 5 ex5

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'url')

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'url')


#below changed chapter 5 ex , added PageAdmin
admin.site.register(Page,PageAdmin)

# Update the registration to include this customised interface - 6.3
admin.site.register(Category, CategoryAdmin)

#models for excersises, projects and tutorials 
admin.site.register(project)
admin.site.register(video,VideoAdmin)
admin.site.register(UserProfile)
admin.site.register(exercises)
admin.site.register(tutorials)
