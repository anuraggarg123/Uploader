from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls')),
    path('',include('delete.urls')),
    path('',include('home.urls')),
    path('',include('signup.urls')),
    path('',include('login.urls')),
    path('',include('show.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # we use this pattern so that django will be known that it is the pattern to find media files
