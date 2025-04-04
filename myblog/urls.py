from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Include blog app's URLs
    path('accounts/', include('django.contrib.auth.urls')),  # For login/logout
]
