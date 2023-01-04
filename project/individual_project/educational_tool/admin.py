from django.contrib import admin
from educational_tool.models import Category, Page

#second from.. added in ex5.6
# Register your models here.

#class below created chapter 5 ex5

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'url')

admin.site.register(Category)
#below changed chapter 5 ex , added PageAdmin
admin.site.register(Page,PageAdmin)