from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account_app/', include('account_app.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('images/', include('images.urls', namespace='images')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


"""
https://mysite.com/images/create/?title=%20Django%20and%20
Duke&url=https://upload.wikimedia.org/wikipedia/commons/8/85/Django_
Reinhardt_and_Duke_Ellington_%28Gottlieb%29.jpg
"""