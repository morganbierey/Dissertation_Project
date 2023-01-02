"""individual_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from educational_tool import views
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static

=======
>>>>>>> da5efec9b488fb10c2988553e0965ca90b006e08


urlpatterns = [
    path('', views.index, name='index'),
    path('educational_tool/', include('educational_tool.urls')),
<<<<<<< HEAD
    path('', views.index, name='about/'),
    # The above maps any URLs starting with educational_tool/ to be handled by educational_tool.
    path('admin/', admin.site.urls),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

=======
    # The above maps any URLs starting with educational_tool/ to be handled by educational_tool.
    path('admin/', admin.site.urls),
    
]
>>>>>>> da5efec9b488fb10c2988553e0965ca90b006e08
