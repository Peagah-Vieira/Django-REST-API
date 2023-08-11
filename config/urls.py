from django.contrib import admin
from django.urls import include, path

# My Apps URLs
urlpatterns = [
    path(
        'accounts/',
        include('accounts.urls')
    ),
]

# Django Apps Default URLs
urlpatterns += [
    path('admin/', admin.site.urls),
]