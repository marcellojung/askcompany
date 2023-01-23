"""askcompany URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static #static 
from django.urls import path,include
from django.conf import settings ##django가 global_settings와 app의 settings를 합쳐줌. 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog1/', include('blog1.urls')),
    path('instagram/', include('instagram.urls')),
    
]
if settings.DEBUG:  #debug 상태일때만 미디어 파일 루트를 지정해줌. http://127.0.0.1:8000/media/Cyan.png
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# settings.MEDIA_URL
# settings.MEDIA_ROOT