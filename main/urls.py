from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from decouple import config

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls")),
    path("member/", include("django.contrib.auth.urls")),
    path("member/",include("member.urls")),
] 

# DEBUG = config("DEBUG")

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)