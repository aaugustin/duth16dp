import debug_toolbar
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^__debug__/', include(debug_toolbar.urls)),
]
